import json
from algosdk.v2client import algod
from algosdk import mnemonic, account, transaction
from algorandEjemploAldeco.primero_crearCuenta import Cuenta

# Este ejemplo requiere de 3 cuentas, la cuenta 1 y 2 se asume ya han sido creadas
#  - account_1 necesita de 1001000 microAlgos
#  - account_2 necesita de 2001000 microAlgos
#  - account_3 generada en código, se le transferirán 1000000 microAlgos 
# Para la cuenta 1 y 2 incluye los mnemonicos correspondientes  
# Para la cuenta 3, guarda el mnemonico creado para consultarlo en el futuro

# never use mnemonics in code, for demo purposes only
# user declared account mnemonics for account1 and account2
mnemonic_1 = ""
mnemonic_2 = ""

# Parametros de conexión para AlgoNode
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

# Funcion de utilidad para obtener una dirección
def get_address(mn):
    pk_account_a = mnemonic.to_private_key(mn)
    address = account.address_from_private_key(pk_account_a)
    print("Address :", address)
    return address

# Funcion para generar una cuenta nueva
def generate_new_account():
    private_key, address = account.generate_account()
    print("Created new account: ", address)
    print("Generated mnemonic: \"{}\"".format(
        mnemonic.from_private_key(private_key)))
    return address

# Funcion para mostrar el balance de una cuenta
def display_account_algo_balance(client, address):
    account_info = client.account_info(address)
    print("... {}: {} microAlgos".format(address, account_info["amount"]))

def intercambio_activo_grupo(algod_client, lista_de_cuentas):
    '''
    params = algod_client.suggested_params()

    txn = AssetTransferTxn(
        sender = sender_address,
        sp = params,
        receiver = receiver_adderss,
        amt = amount,
        index = asset_id)
    
    # Se firma la transacción
    stxn = SEGUNDO.firmar_transaccion(txn,sender_private_key)

    # Se envia la transacción a la red
    confirmed_txn, txid = SEGUNDO.enviar_transaccion(algod_client,stxn)
    print("... Activo transferido")

    return confirmed_txn, txid
    '''

    params = algod_client.suggested_params()

    print("\n... Creating transactions")
    lista_de_transacciones = []

    for sender,receiver,amount,asset_id in lista_de_cuentas:
        txn = transaction.AssetTransferTxn(sender.direccion, params, receiver.direccion, amount, asset_id)
        lista_de_transacciones.append((txn,sender))
        print("... txn: from {} to {} for {} microAlgos".format(sender.nombre_cuenta, receiver.nombre_cuenta, amount))
        print("... created txn: ", txn.get_txid())

    print("\n... Grouping transactions")
    # calcular el id de grupo e incluirlo en cada transaccion
    
    group_id = transaction.calculate_group_id([txn for txn,_ in lista_de_transacciones])
    print("... computed groupId: ", group_id)
    for txn, _ in lista_de_transacciones:
        txn.group = group_id
    
    # firmando transacciones
    print("\n... Signing transactions")
    lista_de_transacciones_firmadas = []
    for txn,sender in lista_de_transacciones:
        signed_txn = txn.sign(sender.llave_privada)
        print(f"... account:{sender.nombre_cuenta} signed tx:{signed_txn.get_txid()}")
        lista_de_transacciones_firmadas.append(signed_txn)

    # creando el grupo de transacciones
    print("\n... Assembling transaction group")
    signedGroup = []
    for stxn in lista_de_transacciones_firmadas:
        signedGroup.append(stxn)

    # enviando grupo de transacciones
    print("\n... Sending transaction group")
    tx_id = algod_client.send_transactions(signedGroup)

    # esperando confirmacion
    confirmed_txn = transaction.wait_for_confirmation(algod_client, tx_id, 4)
    print("\n... txID: {}".format(tx_id), " confirmed in round: {}".format(confirmed_txn.get("confirmed-round", 0)))   

    # imprimiendo balances
    print("\n... Final balances:")
    for sender,receiver,amount, _ in lista_de_cuentas:
        display_account_algo_balance(algod_client, sender.direccion)
        display_account_algo_balance(algod_client, receiver.direccion)
        print()

    # mostrando confirmaciones de transacciones
    for txn,_ in lista_de_transacciones:
        confirmed_txn = algod_client.pending_transaction_info(txn.get_txid())
        print("\nTransaction information: {}".format(json.dumps(confirmed_txn, indent=4)))

def group_transactions():
    
    algod_client = algod.AlgodClient(algod_token, algod_address)
    print("Loading two existing accounts TO SIGN, and account_3 to recieve")
    account_1 = get_address(mnemonic_1)
    account_2 = get_address(mnemonic_2)
    account_3 = generate_new_account()
    print("!! NOTICE !! Please retain the above generated \"25-word mnemonic passphrase\" for future use.")
    sk_1 = mnemonic.to_private_key(mnemonic_1)
    sk_2 = mnemonic.to_private_key(mnemonic_2)

    print("Initial balances:")
    display_account_algo_balance(algod_client, account_1)
    display_account_algo_balance(algod_client, account_2)
    display_account_algo_balance(algod_client, account_3)

    params = algod_client.suggested_params()
    print("Creating transactions...")
    # de la cuenta 1 a la cuenta 3
    sender = account_1
    receiver = account_3
    amount = 100000
    txn_1 = transaction.PaymentTxn(sender, params, receiver, amount)
    print("...txn_1: from {} to {} for {} microAlgos".format(sender, receiver, amount))
    print("...created txn_1: ", txn_1.get_txid())
    # de la cuenta 2 a la cuenta 1
    sender = account_2
    receiver = account_1
    amount = 200000
    txn_2 = transaction.PaymentTxn(sender, params, receiver, amount)
    print("...txn_2: from {} to {} for {} microAlgos".format(sender, receiver, amount))
    print("...created txn_2: ", txn_2.get_txid())

    print("Grouping transactions...")
    # calcular el id de grupo e incluirlo en cada transaccion
    
    group_id = transaction.calculate_group_id([txn_1, txn_2])
    print("...computed groupId: ", group_id)
    txn_1.group = group_id
    txn_2.group = group_id

    # firmando transacciones
    print("Signing transactions...")
    stxn_1 = txn_1.sign(sk_1)
    print("...account1 signed txn_1: ", stxn_1.get_txid())
    stxn_2 = txn_2.sign(sk_2)
    print("...account2 signed txn_2: ", stxn_2.get_txid())

    # creando el grupo de transacciones
    print("Assembling transaction group...")
    signedGroup = []
    signedGroup.append(stxn_1)
    signedGroup.append(stxn_2)

    # enviando grupo de transacciones
    print("Sending transaction group...")
    tx_id = algod_client.send_transactions(signedGroup)

    # esperando confirmacion

    confirmed_txn = transaction.wait_for_confirmation(algod_client, tx_id, 4)
    print("txID: {}".format(tx_id), " confirmed in round: {}".format(
    confirmed_txn.get("confirmed-round", 0)))   
    # imprimiendo balances
    print("Final balances:")
    display_account_algo_balance(algod_client, account_1)
    display_account_algo_balance(algod_client, account_2)
    display_account_algo_balance(algod_client, account_3)

    # mostrando confirmaciones de transacciones
    # tx1
    confirmed_txn = algod_client.pending_transaction_info(txn_1.get_txid())
    print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))

    # tx2
    confirmed_txn = algod_client.pending_transaction_info(txn_2.get_txid())
    print("Transaction information: {}".format(json.dumps(confirmed_txn, indent=4)))


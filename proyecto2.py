import os
import algorandEjemploAldeco.primero_crearCuenta as PRIMERO
import algorandEjemploAldeco.segundo_first_transaction_example as SEGUNDO
import algorandEjemploAldeco.tercero_admin_asset as TERCERO
### CREACION DE CUENTAS INVOLUCRADAS EN EL PROYECTO ####
'''
1. (BM) Banco de Mexico: Este es el ente que creara la moneda digital a ser utilizada como dinero fiat.
2. (C) Cuenta ciudadanos: Este ente representara a un conjunto de ciudadanos que pagana sus impuestos a hacienda.
3. (S) SAT: Este ente representará al Servicio de Administración Tributaria, el cual es el encargado de recaudar los impuestos de los ciudadanos. Y redigirigir parte de lo recaudado a Hospitales Publicos.
4. (H) Hospital: Este ente representará a un Hospital Publico, el cual recibirá parte de los impuestos recaudados por el SAT. Además se encargara de la creacion de nuevos activos que reprentaran isumos medicos.
5. (P) Proveedores: Este ente se encargará de suministrar insumos medicos al Hospital. Recibiendo activos de una moneda y entregando activos de otro tipo, en este caso insumos médicos solicitaos por el Hospital.
6. (D) Doctor[a]: Este ente representará a un doctor o doctora que trabaja en el Hospital. El doctor recibirá activos de insumos medicos y los entregará a los pacientes.
7. (E) Enfermer[o|a]: Este ente representará a un enfermero o enfermera que trabaja en el Hospital. El enfermero recibirá activos de insumos medicos y los entregará a los pacientes.
'''

# ¡Importante¡: En este proyecto se almacenan las llaves privadas de las cuentas en un archivo de texto solo con fines didacticos. Idealmente, las llaves privadas deben ser almacenadas en un lugar seguro y no deben ser compartidas con nadie.

nombre_archivo = "cuentas.txt"

if os.path.exists(nombre_archivo):
    # Si el archivo con las direcciones de las cuentas y sus PKs existe, entonces ya no se crean nuevas cuentas.
    print(f"El archivo '{nombre_archivo}' existe. Ya hay cuentas creadas.")
    lista_de_cuentas = PRIMERO.leer_cuentas_deArchivo(nombre_archivo)

    cuenta_BM = lista_de_cuentas[0]
    cuenta_C = lista_de_cuentas[1]
    cuenta_S = lista_de_cuentas[2]
    cuenta_H = lista_de_cuentas[3]
    cuenta_P = lista_de_cuentas[4]
    cuenta_D = lista_de_cuentas[5]
    cuenta_E = lista_de_cuentas[6]
else:
    # Si el archivo con las direcciones de las cuentas y sus PKs no existe, entonces se crean nuevas cuentas.
    # Generando llave privada de cuenta A y su dirección
    print(f"El archivo '{nombre_archivo}' no existe. Se crean nuevas cuentas.")

    cuenta_BM, _ = PRIMERO.generar_cuenta()
    cuenta_C, _ = PRIMERO.generar_cuenta()
    cuenta_S, _ = PRIMERO.generar_cuenta()
    cuenta_H, _ = PRIMERO.generar_cuenta()
    cuenta_P, _ = PRIMERO.generar_cuenta()
    cuenta_D, _ = PRIMERO.generar_cuenta()
    cuenta_E, _ = PRIMERO.generar_cuenta()

    lista_de_cuentas = [cuenta_BM, cuenta_C, cuenta_S, cuenta_H, cuenta_P, cuenta_D, cuenta_E]

    for cuenta in lista_de_cuentas:
        # Almacenando en un archivo de texto la llave privada y la dirección de la cuenta A
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{cuenta.direccion},{cuenta.llave_privada}\n")

print("Cuenta BM:", cuenta_BM.direccion)
print("Cuenta C:", cuenta_C.direccion)
print("Cuenta S:", cuenta_S.direccion)
print("Cuenta H:", cuenta_H.direccion)
print("Cuenta P:", cuenta_P.direccion)
print("Cuenta D:", cuenta_D.direccion)
print("Cuenta E:", cuenta_E.direccion)

### CREACION DE ACTIVOS ###
'''
Para el proyecto se crearan 2 activos:
1. (MXN) Peso Mexicano: Este activo representará la moneda fiat de Mexico.
2. Insumos Medicos: Este activo o activos representarán los insumos médicos que se utilizaran en el Hospital.
    a) (caja_jer) Insumo Medico 1: Este activo representará jeringas.
    b) (caja_cub) Insumo Medico 2: Este activo representará cubrebocas.

El activo MXN será creado por el Banco de México (BM) y sera quien pague los fees en Algorand por la creacion de este activo.
Los activos de insumos medicos seran creados por el Hospital (H) y sera quien pague los fees en Algorand por la creacion de estos activos.
'''

# Creando activo MXN
activo_1_nombre = "MXN"
activo_1_unidad = "peso(s)"
creador_activo_1 = "BM"

print(f"\n### Creando activo {activo_1_nombre} ###")
print(f"Cuenta creadora del activo {activo_1_unidad} es ({creador_activo_1}), con dirección: {cuenta_BM.direccion}\n")

# ¡Importante¡: No olvides añadir fondos a la cuenta creadora del activo
# URL: https://testnet.algoexplorer.io/dispenser
#input(f"Presiona enter hasta haber añadido fondos a la cuenta del creador del activo:{creador_del_activo.direccion}\n")

# Conexión con el cliente
algod_client = SEGUNDO.conexion_con_cliente_algod(red="algonode")

# Revisando saldo de la cuenta
saldo_BM, account_info_BM = SEGUNDO.verficar_balance_cuenta(algod_client, cuenta_BM.direccion)
print(f"Saldo de la cuenta ({creador_activo_1}) es: {saldo_BM} microAlgos\n")

if(saldo_BM > 10000):
    # Creamos un activo
    '''
        El activo MXN tendrá las siguientes características:
        1. Sera creado por el Banco de México (BM)
        2. Será administrado por el Banco de México (BM)
        3. La cuenta de reserva será la cuenta del Banco de México (BM)
        4. La cuenta de congelación será la cuenta del Banco de México (BM)
        5. La cuenta de revocación será la cuenta del Banco de México (BM)
    '''
    sender = cuenta_BM.direccion
    sender_pk = cuenta_BM.llave_privada
    manager = cuenta_BM.direccion
    reserve = cuenta_BM.direccion
    freeze = cuenta_BM.direccion
    clawback = cuenta_BM.direccion

    confirmed_txn, tx_id = TERCERO.crear_activo(
        algod_client,
        sender_pk, 
        sender, 
        manager, 
        reserve, 
        freeze, 
        clawback,
        asset_name=activo_1_nombre, # Max 8 caracteres
        unit_name=activo_1_unidad # Max 8 caracteres
    )

    TERCERO.imprimir_transaccion_activo(algod_client, confirmed_txn, tx_id, cuenta_BM.direccion)
else:
    print("No hay fondos suficientes en la cuenta para crear el activo.")

# Creando activo caja_jer
activo_2_nombre = "caja_jer"
activo_2_unidad = "jeringa"
creador_activo_2 = "H"

print(f"\n### Creando activo {activo_2_nombre} ###")
print(f"Cuenta creadora del activo {activo_2_unidad} es ({creador_activo_2}), con dirección: {cuenta_H.direccion}\n")

# ¡Importante¡: No olvides añadir fondos a la cuenta creadora del activo
# URL: https://testnet.algoexplorer.io/dispenser
#input(f"Presiona enter hasta haber añadido fondos a la cuenta del creador del activo:{creador_del_activo.direccion}\n")

# Revisando saldo de la cuenta
saldo_H, account_info_H = SEGUNDO.verficar_balance_cuenta(algod_client, cuenta_H.direccion)
print(f"Saldo de la cuenta ({creador_activo_2}) es: {saldo_BM} microAlgos\n")

if(saldo_H > 10000):
    # Creamos un activo
    '''
        El activo MXN tendrá las siguientes características:
        1. Sera creado por el Banco de México (BM)
        2. Será administrado por el Banco de México (BM)
        3. La cuenta de reserva será la cuenta del Banco de México (BM)
        4. La cuenta de congelación será la cuenta del Banco de México (BM)
        5. La cuenta de revocación será la cuenta del Banco de México (BM)
    '''
    sender = cuenta_H.direccion
    sender_pk = cuenta_H.llave_privada
    manager = cuenta_H.direccion
    reserve = cuenta_H.direccion
    freeze = cuenta_H.direccion
    clawback = cuenta_H.direccion

    confirmed_txn, tx_id = TERCERO.crear_activo(
        algod_client,
        sender_pk, 
        sender, 
        manager, 
        reserve, 
        freeze, 
        clawback,
        asset_name=activo_2_nombre, # Max 8 caracteres
        unit_name=activo_2_unidad # Max 8 caracteres
    )

    TERCERO.imprimir_transaccion_activo(algod_client, confirmed_txn, tx_id, cuenta_H.direccion)
else:
    print("No hay fondos suficientes en la cuenta para crear el activo.")
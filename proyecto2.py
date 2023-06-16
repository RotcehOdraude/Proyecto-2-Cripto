import os
import algorandEjemploAldeco.primero_crearCuenta as PRIMERO
import algorandEjemploAldeco.segundo_first_transaction_example as SEGUNDO
import algorandEjemploAldeco.tercero_admin_asset as TERCERO
import algorandEjemploAldeco.cuarto_atomic_transfer as CUARTO

### CREACION DE CUENTAS INVOLUCRADAS EN EL PROYECTO ####
'''
1. (BM) Banco de Mexico: Este es el ente que creara la moneda digital a ser utilizada como dinero fiat.
2. (C) Cuenta ciudadanos: Este ente representara a un conjunto de ciudadanos que pagan sus impuestos a hacienda.
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
    cuenta_Paciente1 = lista_de_cuentas[7]
    cuenta_Paciente2 = lista_de_cuentas[8]

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
    cuenta_Paciente1 = PRIMERO.generar_cuenta()
    cuenta_Paciente2 = PRIMERO.generar_cuenta()

    lista_de_cuentas = [cuenta_BM, cuenta_C, cuenta_S, cuenta_H, cuenta_P, cuenta_D, cuenta_E]

    for cuenta in lista_de_cuentas:
        # Almacenando en un archivo de texto la llave privada y la dirección de la cuenta A
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"{cuenta.direccion},{cuenta.llave_privada}\n")

cuenta_BM.nombre_cuenta = "(BM)"
cuenta_C.nombre_cuenta = "(C)"
cuenta_S.nombre_cuenta = "(S)"
cuenta_H.nombre_cuenta = "(H)"
cuenta_P.nombre_cuenta = "(P)"
cuenta_D.nombre_cuenta = "(D)"
cuenta_E.nombre_cuenta = "(E)"
cuenta_Paciente1.nombre_cuenta = "(Paciente1)"
cuenta_Paciente2.nombre_cuenta = "(Paciente2)"

print("Cuenta BM:", cuenta_BM.direccion)
print("Cuenta C:", cuenta_C.direccion)
print("Cuenta S:", cuenta_S.direccion)
print("Cuenta H:", cuenta_H.direccion)
print("Cuenta P:", cuenta_P.direccion)
print("Cuenta D:", cuenta_D.direccion)
print("Cuenta E:", cuenta_E.direccion)
print("Cuenta Paciente1:", cuenta_Paciente1.direccion)
print("Cuenta Paciente2:", cuenta_Paciente2.direccion)

input(f"Presiona enter hasta haber añadido fondos a la(s) cuenta(s)\n")

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

    confirmed_txn_activo_1, tx_id_activo_1 = TERCERO.crear_activo(algod_client, sender_pk, sender, manager, reserve, freeze, clawback, asset_name=activo_1_nombre, unit_name=activo_1_unidad) # Max 8 caracteres para ambos unit_name y asset_name

    TERCERO.imprimir_transaccion_activo(algod_client, confirmed_txn_activo_1, tx_id_activo_1, cuenta_BM.direccion)

    # Obtenemos el id del activo (peso)
    asset_id_peso = TERCERO.obtener_asset_id(algod_client,tx_id_activo_1)
else:
    print("No hay fondos suficientes en la cuenta para crear el activo.")


### TRANSACCIONES ###
'''
Para este proyecto se plantea el siguiente escenario de transacciones:
    1. El Banco de México (BM) crea la moneda (peso) que utilizamos para realizar transacciones entre personas [Completado]
    2. El Banco de México (BM) realiza una transaccion/es a los ciudadanos de un país, les el activo (pesos)
    3. Los ciudadanos (C) pagan sus impuesto y realizan una transaccion al SAT(S)
    4. El SAT (S) reparte lo recaudado y realiza una transacción al hospital (H)
    5. El proveedor (P) es una entidad que crea activos de distintos insumos medicos, para este proyecto solo seran jerigas. 
    6. El hospital (H) realiza una transacción al proveedor (P) para adquirir insumos medicos.El hospital podrá realizar transacciones con los empleados del hospital, Doctor (D) y Enfermera (E) y con el proveedor de insumos medicos (P)
    7. El proveedor (P) realiza una transacción al hospital (H) para enviarle los insumos medicos y recibir el pago en pesos.
    8. El hospital (H) realiza una transacción de insumos medicos ya sea al doctor (D) o a la enfermera (E)
    9. Por último el doctor (D) o la enfermera (E) realizan una transacción al paciente (P) quien es el beneficiario final de toda esta cadena de transacciones.

 '''

    # TRANSACCIÓN 1: Banco de México (BM) crea activo (peso)[Completado]

# Activo 1 = peso
# Activo 2 = caja de jeringas

    # TRANSACCIÓN 2: Banco de México (BM) ------> Ciudadanos (C); (BM) envía activo (peso) a los ciudadanos (C)
print(f"\n### (BM) enviando activo (peso) a los ciudadanos (C) ###")

# ¡Importante¡: No olvides añadir fondos a la cuenta que va a pagar por la transacción, en este caso Ciudadano (C).

# Primero el ciudadando (C) debe hacer una operación OPT-IN para poder recibir el activo (peso)
confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_peso, cuenta_C.direccion, cuenta_C.llave_privada)

TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_BM, cuenta_C)

# Ahora el ciudadano (C) puede recibir el activo (peso)
confirmed_txn, txid = TERCERO.transferir_activo(algod_client ,cuenta_BM.direccion, cuenta_BM.llave_privada, cuenta_C.direccion, 90, asset_id_peso)


TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_BM, cuenta_C)

    # TRANSACCIÓN 3: Ciudadanos (C) ------> SAT (S); (C) envía activo (peso) al SAT (S)
print(f"\n### (C) enviando activo (peso) al SAT (S) ###")

# ¡Importante¡: No olvides añadir fondos a la cuenta que va a pagar por la transacción, en este caso Ciudadano (S).

# Primero el SAT (S) debe hacer una operación OPT-IN para poder recibir el activo (peso)
confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_peso, cuenta_S.direccion, cuenta_S.llave_privada)

TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_C, cuenta_S)

# Ahora el SAT (S) puede recibir el activo (peso)
confirmed_txn, txid = TERCERO.transferir_activo(algod_client ,cuenta_C.direccion, cuenta_C.llave_privada, cuenta_S.direccion, 70, asset_id_peso)

TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_C, cuenta_S)

    # TRANSACCIÓN 4: SAT (S) ------> Hospital (H); (S) envía activo (peso) al Hospital (H)
print(f"\n### (S) enviando activo (peso) al Hospital (H) ###")

confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_peso, cuenta_H.direccion, cuenta_H.llave_privada)

TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_S, cuenta_H)

confirmed_txn, txid = TERCERO.transferir_activo(algod_client ,cuenta_S.direccion, cuenta_S.llave_privada, cuenta_H.direccion, 40, asset_id_peso)

TERCERO.print_saldo_cuentas(algod_client, asset_id_peso,cuenta_S, cuenta_H)

    # TRANSACCIÓN 5: PROVEEDOR (P) crea activo (caja de jeringas);
# Creando activo caja_jer (caja de jeringas) 
activo_2_nombre = "caja_jer"
activo_2_unidad = "jeringa"
creador_activo_2 = "P"

print(f"\n### Creando activo {activo_2_nombre} ###")
print(f"Cuenta creadora del activo {activo_2_unidad} es ({creador_activo_2}), con dirección: {cuenta_P.direccion}\n")

# ¡Importante¡: No olvides añadir fondos a la cuenta creadora del activo
# URL: https://testnet.algoexplorer.io/dispenser


# Revisando saldo de la cuenta
saldo_P, account_info_P = SEGUNDO.verficar_balance_cuenta(algod_client, cuenta_P.direccion)
print(f"Saldo de la cuenta ({creador_activo_2}) es: {saldo_P} microAlgos\n")

if(saldo_P > 10000):
    # Creamos un activo
    '''
        El activo caja_jer tendrá las siguientes características:
        1. Sera creado por el Hospital (H)
        2. Será administrado por el Hospital (H)
        3. La cuenta de reserva será la cuenta del Hospital (H)
        4. La cuenta de congelación será la cuenta del Hospital (H)
        5. La cuenta de revocación será la cuenta del Hospital (H)
    '''
    sender = cuenta_P.direccion
    sender_pk = cuenta_P.llave_privada
    manager = cuenta_H.direccion
    reserve = cuenta_H.direccion
    freeze = cuenta_H.direccion
    clawback = cuenta_H.direccion

    confirmed_txn_activo_2, tx_id_activo_2 = TERCERO.crear_activo(algod_client, sender_pk, sender, manager, reserve, freeze, clawback, asset_name=activo_2_nombre, unit_name=activo_2_unidad,total=50) # Max 8 caracteres para ambos unit_name y asset_name

    TERCERO.imprimir_transaccion_activo(algod_client, confirmed_txn_activo_2, tx_id_activo_2, cuenta_P.direccion)
    # Obtenemos el id del activo (peso)
    asset_id_jeringas = TERCERO.obtener_asset_id(algod_client,tx_id_activo_2)
else:
    print("No hay fondos suficientes en la cuenta para crear el activo.")

#TERCERO.print_saldo_cuentas(algod_client, asset_id_jeringas,cuenta_P, cuenta_P)


########## TRANSACCION CIRCULAR ##########
    # TRANSACCIÓN 6: Hospital (H) ------> Proveedores (P); (H) envía activo (peso) al proveedor (P)
    # TRANSACIOÓN 7: Proveedores (P) ------> Hospital (H); (P) envía activo (caja de jeringas) al Hospital (H)

print(f"\n### TRANSACCIÓN CIRCULAR ###")

confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_peso, cuenta_P.direccion, cuenta_P.llave_privada)
confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_jeringas, cuenta_H.direccion, cuenta_H.llave_privada)

CUARTO.intercambio_activo_grupo(algod_client, [(cuenta_H, cuenta_P, 5, asset_id_peso),(cuenta_P,cuenta_H ,5 ,asset_id_jeringas)])

    # TRANSACCIÓN 8: Hospital (H) ------> Doctor@ (D); (H) envía activo (caja de jeringas) al Doctor@ (D)
    # TRANSACCIÓN 8: Hospital (H) ------> Enferfer@ (E); (H) envía activo (caja de jeringas) al Enfermer@ (E)
print(f"\n### (H) enviando activo (jeringa) al Doctor (D) ###")

confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_jeringas, cuenta_D.direccion, cuenta_D.llave_privada)

TERCERO.print_saldo_cuentas(algod_client, asset_id_jeringas,cuenta_H, cuenta_D)

confirmed_txn, txid = TERCERO.transferir_activo(algod_client ,cuenta_H.direccion, cuenta_H.llave_privada, cuenta_D.direccion, 3, asset_id_jeringas)

TERCERO.print_saldo_cuentas(algod_client, asset_id_jeringas,cuenta_H, cuenta_D)

    # TRANSACCIÓN 9: Doctor@ (D) ------> Paciente (P); (D) envía activo (caja de jeringas) al Paciente (P)

print(f"\n### (D) enviando activo (jeringa) al Paciente (P) ###")

confirmed_txn, txid = TERCERO.opt_in(algod_client, asset_id_jeringas, cuenta_Paciente1.direccion, cuenta_Paciente1.llave_privada)

TERCERO.print_saldo_cuentas(algod_client, asset_id_jeringas,cuenta_D, cuenta_Paciente1)

confirmed_txn, txid = TERCERO.transferir_activo(algod_client ,cuenta_D.direccion, cuenta_D.llave_privada, cuenta_Paciente1.direccion, 1, asset_id_jeringas)

TERCERO.print_saldo_cuentas(algod_client, asset_id_jeringas,cuenta_D, cuenta_Paciente1)
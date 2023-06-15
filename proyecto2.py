import os
import algorandEjemploAldeco.primero_crearCuenta as PRIMERO
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
    print("El archivo existe. Ya hay cuentas creadas.")
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
    print("El archivo no existe. Se crean nuevas cuentas.")

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

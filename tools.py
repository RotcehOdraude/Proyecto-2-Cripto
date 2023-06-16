import os
import sys
import algorandEjemploAldeco.primero_crearCuenta as PRIMERO

# Obtener los argumentos de la línea de comandos
argumentos = sys.argv

# El primer argumento (índice 0) es el nombre del script, los siguientes son los argumentos
# Puedes acceder a ellos mediante su índice
# Por ejemplo, para obtener el primer argumento, usarías argumentos[1]
# Ten en cuenta que los argumentos son cadenas de texto (strings)

def main():
    print(f"sys.argv: {argumentos}")
    if len(argumentos) == 1:
        print("TOOL: No elegiste ninguna herramienta.")
    elif (argumentos[1] == "imprimir"):
        print("TOOL:", argumentos[1])
        imprimir_cuentas_existentes()
    elif (argumentos[1] == "crear"):
        print("TOOL:", argumentos[1])
        crear_cuentas(argumentos[2])

def crear_cuentas(numero_de_cuentas):
    for i in range(int(numero_de_cuentas)):
        print("Creando cuenta", i)
        cuenta, _ = PRIMERO.generar_cuenta()
        print(f"Cuenta: {cuenta.direccion}, \nClave: {cuenta.llave_privada}")

def imprimir_cuentas_existentes(nombre_archivo = "cuentas.txt"):
    #nombre_archivo = "cuentas.txt"

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

    print("Cuenta BM:", cuenta_BM.direccion)
    print("Cuenta C:", cuenta_C.direccion)
    print("Cuenta S:", cuenta_S.direccion)
    print("Cuenta H:", cuenta_H.direccion)
    print("Cuenta P:", cuenta_P.direccion)
    print("Cuenta D:", cuenta_D.direccion)
    print("Cuenta E:", cuenta_E.direccion)

main()
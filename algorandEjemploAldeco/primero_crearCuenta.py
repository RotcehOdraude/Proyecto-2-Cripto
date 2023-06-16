import algosdk

# Haciendo una estructura para la cuenta
class Cuenta:
    def __init__(self, llave_privada, direccion ):
        self.llave_privada = llave_privada
        self.direccion = direccion
        self.nombre_cuenta = ""

def generar_cuenta():
    """
    Genera una nueva llave privada y la dirección de cuenta asociada.

    Returns:
        Tuple: Una tupla que contiene (la dirección de cuenta, la llave privada generada) y el mnemónico de la llave privada.
    
    Raises:
        None.

    Example:
        private_key, account_address = generar_cuenta()
    """
    # Generate a fresh private key and associated account address
    private_key, account_address = algosdk.account.generate_account()

    # Convert the private key into a mnemonic which is easier to use
    mnemonic = algosdk.mnemonic.from_private_key(private_key)

    # Wrapping the private key and address into a class
    account = Cuenta(private_key, account_address)

    return account, mnemonic

def leer_cuentas_deArchivo(archivo):
    """
    Lee un archivo y devuelve una lista de objetos Cuenta.

    Parámetros:
    - archivo (str): Ruta del archivo a leer.

    Retorna:
    - cuentas (list): Lista de objetos 'Cuenta' creados a partir de los datos del archivo.

    La función lee el archivo especificado y crea objetos Cuenta a partir de cada línea válida.
    Cada línea del archivo debe contener una dirección y una clave, separadas por una coma.
    Se eliminan los espacios en blanco al inicio y final de cada línea.
    Los objetos Cuenta se agregan a la lista cuentas, que se devuelve al final de la función.
    """
    cuentas = []
    with open(archivo, "r") as file:
        for linea in file:
            linea = linea.strip()  # Eliminar espacios en blanco al inicio y final de la línea
            if linea:
                direccion, clave = linea.split(",")  # Dividir la línea en clave y dirección
                cuentas.append(Cuenta(clave, direccion))  
    return cuentas
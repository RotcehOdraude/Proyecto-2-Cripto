# Proyecto 2 Cripto

A continuación se detallan los pasos para poner en marcha el proyecto en tu entorno local.

## Pasos para poner en marcha el proyecto

1. **Clonar el repositorio:** Clona el repositorio del proyecto en tu máquina local.

    ```shell
    git clone https://github.com/RotcehOdraude/Proyecto-2-Cripto.git
    ```

2. **Crear un entorno virtual:** Crea un nuevo entorno virtual llamado `algorand_venv`.

   1. Abre una terminal o línea de comandos en tu sistema operativo.

   2. Asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando el siguiente comando:

      ``` shell
      python --version
      ```

   3. Si no tienes Python 3 instalado, debes instalarlo antes de continuar. Puedes descargarlo desde el sitio web oficial de Python [Python Org](https://www.python.org) e instalarlo siguiendo las instrucciones correspondientes a tu sistema operativo.

   4. Una vez que tienes Python instalado, asegúrate de tener la herramienta `venv` instalada. Puedes verificarlo ejecutando el siguiente comando:

      ``` shell
      python -m venv --help
      ```

   5. Ahora estás listo para crear el entorno virtual. En la terminal, navega hasta el directorio donde deseas crear el entorno virtual o especifica la ruta completa al crearlo. Ejecuta el siguiente comando para crear el entorno virtual:

      ``` shell
      python -m venv algorand_venv
      ```

   6. Se creará un directorio llamado "algorand_venv" que contendrá los archivos del entorno virtual.

3. **Activar el entorno virtual:** Activa el entorno virtual recién creado.

   - En Windows:

    ``` bash
    algorand_venv\Scripts\activate
    ```

   - En macOS/Linux:

    ``` shell
    source myenv/bin/activate
    ```

4. **Instalar el paquete py-algorand-sdk**: Instala el paquete `py-algorand-sdk`, que es necesario para el funcionamiento del proyecto.

    ``` shell
    pip install py-algorand-sdk
    ```

## Requisitos previos

- Python 3.x instalado en tu máquina.
- Git instalado en tu máquina.

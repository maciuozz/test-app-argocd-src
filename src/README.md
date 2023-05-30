<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [simple-fast-api](#simple-fast-api)
  - [Descripcion](#descripcion)
  - [Software necesario](#software-necesario)
  - [Ejecución de código](#ejecuci%C3%B3n-de-c%C3%B3digo)
    - [Prerequisitos](#prerequisitos)
    - [Arrancar servidor](#arrancar-servidor)
    - [Ejecución de tests](#ejecuci%C3%B3n-de-tests)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# simple-fast-api

## Descripcion

El objetivo de esta práctica es crear un ejemplo de servidor sencillo utilizando [fastapi](https://fastapi.tiangolo.com/)

## Software necesario

Es necesario disponer del siguiente software:

- `Python` en versión `3.8.5` o superior, disponible para los diferentes sistemas operativos en la [página oficial de descargas](https://www.python.org/downloads/release/python-385/)

- `virtualenv` para podes instalar las librerías necesarias de Python, se puede instalar a través del siguiente comando:

    ```sh
    pip3 install virtualenv
    ```

## Ejecución de código

### Prerequisitos

1. Crear de virtualenv en la raíz del directorio para poder instalar las librerías necesarias:

    ```sh
    python3.8 -m venv venv
    ```

2. Activar el virtualenv creado en el directorio `venv` en el paso anterior:

    ```sh
    source venv/bin/activate
    ```

3. Librerías necesarias de Python, recogidas en el fichero `requirements.txt`, es posible instalarlas a través del siguiente comando:

    ```sh
    pip3 install -r requirements.txt
    ```

### Arrancar servidor

1. Activar el virtualenv creado anteriormente, **sólo en caso de no estar ya activado**:

    ```sh
    source venv/bin/activate
    ```

2. Lanzar el servidor:

    ```sh
    python3 application/app.py
    ```

    **En caso de que en la primera ejecución el servidor falle mostrando un error con el mensaje `from fastapi import FastAPI ModuleNotFoundError: No module named 'fastapi'` será necesario desactivar y volver a activar el entorno virtual creado** ejecutando los siguientes comandos:

    ```sh
    deactivate
    source venv/bin/activate
    ```

3. Probar las diferentes peticiones una vez levantado el servidor:
    - Probar una petición al endpoint `/`

        ```sh
        curl -X 'GET' \
        'http://0.0.0.0:8081/' \
        -H 'accept: application/json'
        ```

        Debería devolver la siguiente respuesta:

        ```json
        {"message":"Hello World"}
        ```

    - Probar una petición al endpoint `/health`

        ```sh
        curl -X 'GET' \
        'http://0.0.0.0:8081/health' \
        -H 'accept: application/json'
        ```

        Debería devolver la siguiente respuesta.

        ```json
        {"health": "ok"}
        ```

### Ejecución de tests

- Ejecución de tests:

    ```sh
    pytest
    ```

- Ejecución de tests y mostrar cobertura:

    ```sh
    pytest --cov
    ```

- Ejecución de tests y generación de report de cobertura:

    ```sh
    pytest --cov --cov-report=html
    ```

# Codigo python
from fastapi import FastAPI # Importa propio  del framework FastAPI
from typing import List # Importa estandar de python para tipado

# CREACION DE LA APLICACION

app = FastAPI() # Objeto principal de la API (Intancia del framework)

#  BASE DE DATOS SIMULADA  

clientes = [] # Variable global tipo lista alamacenar clientes en memoria

# ENDOPINT RAIZ
@app.get("/") # Decroador propio de FastAPI para metodos GET 

# http exepcion ===> para crear una respuesta

def home(): # Funcion normal (no asincrona por simplicidad)
    return {"Mensaje": "API del Banco funcionando"}

"""
    - @app.get("/") -> Dwfine ruta
    - home() ---> funcion que reposnde
    Retorna JSON automaticamente
"""

# CREAR CLIENTE
@app.post("/clientes") # Decorador para metodo POST
def crear_cliente(nombre: str): # Parametro recibido por query
    cliente = {
        "id" : len(clientes) + 1, # Generacion simple de ID
        "nombre" : nombre
    }

    clientes.append(cliente) # Agrega cliente a lista global

    return cliente # Devuelve cliente creado


# LISTAR CLIENTES GET
@app.get("/clientes", response_model = List[dict]) # Define tipo de respuesta
def listar_clientes():
    return clientes # Devuelve lista completa

# OBTENER CLIENTE POR ID PASO 6

@app.get("/clientes/{cliente_id}") # Ruta con parametros dinamicos

def obtener_cliente(cliente_id : int): # tipo entero
    for cliente in clientes: # recorre lista
        if cliente["id"] == cliente_id:
            return cliente # retorna si encuentra
    
    return {"error" : "Cliente no encontrado"} # manejo basico de errores
# Codigo python
from fastapi import FastAPI, HTTPExcepton # Importa propio  del framework FastAPI
from typing import List # Importa estandar de python para tipado
import asyncio

from database import get_connection

# CREACION DE LA APLICACION

app = FastAPI() # Objeto principal de la API (Intancia del framework)

#  BASE DE DATOS SIMULADA  

citas = [] # Variable global tipo lista alamacenar citas en memoria

# ENDOPINT RAIZ
@app.get("/") # Decorador propio de FastAPI para metodos GET 

# http exepcion ===> para crear una respuesta

def home(): # Funcion normal (no asincrona por simplicidad)
    return {"Mensaje": "API del Banco funcionando"}

"""
    - @app.get("/") -> Dwfine ruta
    - home() ---> funcion que reposnde
    Retorna JSON automaticamente
"""

# CREAR CLIENTE
@app.post("/citas") # Decorador para metodo POST
async def crear_cita(paciente: str, fecha: str): # Parametro recibido por query
    await asyncio.sleep(2) #simulación de proceso lento

    conn = await get_connection()
    cursor = await conn.cursor()

    query = """
    INSERT INTO citas (paciente, fecha, estado)
    VALUES (%s, %s, %s)
    """

    await cursor.execute(query, (paciente, fecha, "activa"))
    await conn.commit()

    await cursor.close()
    conn.close()

    return {"mensaje": "Cita Creada Correctamente"}


# LISTAR citas GET
@app.get("/citas") # Define tipo de respuesta
async def listar_citas():
    conn = await get_connection()
    cursor = await conn.cursor()

    query = "SELECT * FROM citas"

    await cursor.execute(query)
    await conn.commit()

    await cursor.close()
    conn.close()
    return citas

# OBTENER CLIENTE POR ID PASO 6

@app.get("/citas/{paciente}") # Ruta con parametros dinamicos
async def buscar_cita(paciente : str):
    conn = await get_connection()
    cursor = await conn.cursor()

    query = "SELECT * FROM citas WHERE paciente=%s"

    await cursor.execute(query, (paciente,))

    cita = await cursor.fetchone()

    await cursor.close()
    conn.close()

    if not cita:
        raise HTTPExcepton(
            status_code=404,
            detail="Cita no encontrada"
        )
    return cita
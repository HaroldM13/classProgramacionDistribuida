#IMPORTACIONES
import aiomysql #Libreria async par MySQL

#CONFIGURACION PARA CONEXIÓN
DB_CONFIG = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"",
    "db":"citas_db"
}

#FUNCION DE CONEXIÓN

async def get_connection():
    """
        Crea una conexion async con la bd
    """
    return await aiomysql.connect(**DB_CONFIG)
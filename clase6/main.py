from fastapi import FastAPI
import asyncio

app = FastAPI()

contador = 0
lock = asyncio.Lock()

@app.get("/incrementar")
async def incrementar():
    global contador
    async with lock:
        valor_actual = contador
        #Simular una operacion lenta
        await asyncio.sleep(0.1)

        contador = valor_actual + 1

        return {"Contador": contador}
    
@app.post("/reset")
async def resetear_contador():
    global contador #Variable compartida

    contador = 0 #Reiniciamos el valor

    return {"Mensaje": "Contador reiniciado", "Contador": contador}
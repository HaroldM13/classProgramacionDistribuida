import asyncio, httpx

#Semaforo global que permite maximo 10 peticiones concurrentes
semaphore = asyncio.Semaphore(10)

async def peticion(client):
    async with semaphore: #Solo agrega esta linea
        try:
            await client.get("http://127.0.0.1:8000/incrementar")
        except Exception as e:
            print("Error", e)


async def main():
    #Crear cliente con timeout mas largo
    #timeout = httpx.Timeout(30.0) #30 segundos de timeout
    async with httpx.AsyncClient(timeout=10.0) as client:
        await asyncio.gather(*[peticion(client) for _ in range(100)])

asyncio.run(main())
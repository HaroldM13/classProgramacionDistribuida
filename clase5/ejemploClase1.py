import threading
import time

sem = threading.Semaphore(2)

def imprimir(nombre):
    sem.acquire()
    print(nombre, "Esta imprimiedo..")
    time.sleep(3)
    print(nombre, "Termino")
    sem.release()

for i in range(5):
    threading.Thread(
        target=imprimir,
        args=(f"Usuario {i}",)
    ).start()

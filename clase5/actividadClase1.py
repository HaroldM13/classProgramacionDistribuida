import threading
import time

lock = threading.Lock()

asientos = 10

def reservar():
    global asientos
    with lock:
        if asientos > 0:
            asientos -= 1
        print(asientos)


for i in range(50):
    threading.Thread(target=reservar).start()

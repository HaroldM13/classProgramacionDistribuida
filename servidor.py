import socket
import threading

contador_clientes = 0 #Recurso compartido
lock = threading.Lock()

def handle_client(conn, addr):
    global contador_clientes
    print(f"Cliente conectado desde {addr}")
    try:
        with lock:
            contador_clientes += 1
            numero = contador_clientes
            
        print(f"Cliente {numero} atendido desde {addr}")
        student_name = conn.recv(1024).decode()
        response = f"Hola {student_name} eres el cliente numero {numero}"
        conn.sendall(response.encode())
    except Exception as e:
        print(f"Error con {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexion cerrada {addr}")
#Crear server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()

print("Servidor concurrente escuchando...")

while True:
    conn, addr = server.accept()

    #Create a thread per cliente
    #Crear Hilo por cliente
    client_thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    client_thread.start()

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

mensaje = client.recv(1024)
print("Nombre de Estudiante:", mensaje.decode())

client.close()

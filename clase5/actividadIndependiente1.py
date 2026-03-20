import threading

usuarios = 50
cursos = {"Curso 1" : "Español","Curso 2": "Matematicas","Curso 3": "Ingles","Curso 4": "Ciencias","Curso 5": "Sociales","Curso 6":"Etica","Curso 7":"Religion","Curso 8":"Fisica","Curso 9":"Quimica","Curso 10":"Deportes"}
usuario = 0

def reservar():
    global usuario
    if usuario <= usuarios:
        usuario += 1
        print(f"Usuario Numero: {usuario} -> Cursos Registrados: {cursos}")


for i in range(usuarios):
    threading.Thread(target=reservar).start()

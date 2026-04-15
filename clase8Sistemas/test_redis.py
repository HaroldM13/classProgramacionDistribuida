from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


#CREAR CITA
@app.post("/crear_cita")
def crear_cita(hora: str, paciente: str, medico: str):
    lock = r.set(f"citas_{hora}", "ocupado", nx=True, ex=15)
    
    if not lock:
        raise HTTPException(status_code=400, detail="Hora no disponible, Elije otra")
    
    # Crear la cita
    cita_id = r.incr("contador_citas")
    
    # Guardar los datos de la cita
    r.hset(f"cita:{cita_id}", "hora", hora)
    r.hset(f"cita:{cita_id}", "paciente", paciente)
    r.hset(f"cita:{cita_id}", "medico", medico)
    r.hset(f"cita:{cita_id}", "estado", "activa")
    
    r.set(f"citas_{hora}_cita_id", cita_id)
    
    return {"mensaje": "Cita reservada correctamente", "cita_id": cita_id}

#VER CITA
@app.get("/ver_cita")
def ver_cita(cita_id: int):
    # Verificar si la cita existe
    if not r.exists(f"cita:{cita_id}"):
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    # Obtener los datos de la cita
    hora = r.hget(f"cita:{cita_id}", "hora")
    paciente = r.hget(f"cita:{cita_id}", "paciente")
    medico = r.hget(f"cita:{cita_id}", "medico")
    estado = r.hget(f"cita:{cita_id}", "estado")
    
    return {
        "cita_id": cita_id,
        "hora": hora,
        "paciente": paciente,
        "medico": medico,
        "estado": estado
    }

#CANCELAR CITA
@app.delete("/cancelar_cita")
def cancelar_cita(cita_id: int):
    # Verificar si la cita existe
    if not r.exists(f"cita:{cita_id}"):
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    
    hora = r.hget(f"cita:{cita_id}", "hora")
    
    lock_exists = r.exists(f"citas_{hora}")
    
    if lock_exists:
        r.delete(f"citas_{hora}")
        r.delete(f"citas_{hora}_cita_id")
    
    r.hset(f"cita:{cita_id}", "estado", "cancelada")
    
    return {"mensaje": "Cita cancelada correctamente"}

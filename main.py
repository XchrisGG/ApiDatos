from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos qué datos esperamos recibir del móvil/Node
class SensorData(BaseModel):
    heartRate: int
    light: float
    gyro: float

@app.get("/")
def home():
    return {"status": "Microservicio de Análisis Activo"}

@app.post("/analizar")
async def analizar_estres(data: SensorData):
    # ALGORITMO DE PUNTUACIÓN (Lógica Escolar Creíble)
    # Normalizamos valores: BPM ideal es 70, Gyro ideal es 0
    hr_factor = (data.heartRate - 70) * 0.6
    gyro_factor = data.gyro * 10
    light_factor = data.light * 0.05

    score = hr_factor + gyro_factor + light_factor
    
    # Determinamos estado según el puntaje
    if score > 25:
        estado = "Estrés Elevado"
        color = "#FF4B4B"
        sugerencia = "Nivel de agitación alto. Intenta exhalar profundamente."
    elif score > 10:
        estado = "Alerta Moderada"
        color = "#FFA500"
        sugerencia = "Pareces estar inquieto. ¿Te vendría bien un poco de agua?"
    else:
        estado = "Estado Calmo"
        color = "#4CAF50"
        sugerencia = "Tus signos son estables. Sigue así."

    return {
        "score": round(score, 2),
        "estado": estado,
        "color": color,
        "sugerencia": sugerencia,
        "timestamp_analisis": "Calculado por Motor Python"
    }
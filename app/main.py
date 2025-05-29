# app/main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from .executor import ejecutar_codigo

app = FastAPI()

class CodigoPayload(BaseModel):
    codigo: str
    parametros: dict
    detalles_tecnicos: str = ""

@app.post("/run")
async def run_code(payload: CodigoPayload):
    return ejecutar_codigo(payload.codigo, payload.parametros, payload.detalles_tecnicos)
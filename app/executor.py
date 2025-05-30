# app/executor.py
import subprocess
import sys

def instalar_dependencias(paquetes_str):
    paquetes = [p.strip() for p in paquetes_str.split(",") if p.strip()]
    for paquete in paquetes:
        try:
            __import__(paquete)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", paquete])

def ejecutar_codigo(codigo, parametros, detalles_tecnicos):
    try:
        instalar_dependencias(detalles_tecnicos)
        entorno = {}
        exec(codigo, entorno)
        func = entorno.get('ejecutar')
        if not callable(func):
            return {"error": "No se encontró una función 'ejecutar' válida."}
        resultado = func(parametros)
        return { resultado }
    except Exception as e:
        return {"error": str(e)}
# Entornos virtuales: https://docs.python.org/es/3/tutorial/venv.html
# Installation: https://fastapi.tiangolo.com/#installation

from fastapi import FastAPI

app = FastAPI()

def index():
    return "Hola, Fast API"
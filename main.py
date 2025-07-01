from fastapi import FastAPI #importamos
from pydantic import BaseModel
from typing import Optional

app = FastAPI() #instanciamos

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str] 

#rutas:
@app.get("/") #creamos ruta raiz
def index(): 
    return {"message" : "Hola, Fast API. Esto es una funcion tipo Get"}
#funcion que se va a ejecutar

#parametros variables
@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}

@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}

# levanta el servidor: uvicorn main:app --reload
# Entornos virtuales: https://docs.python.org/es/3/tutorial/venv.html
# Installation: https://fastapi.tiangolo.com/#installation

# Documentacion en: http://127.0.0.1:8000/docs
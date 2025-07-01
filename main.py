from fastapi import FastAPI #importamos

app = FastAPI() #instanciamos

#http://127.0.0.1:8000/

@app.get("/") #creamos ruta raiz
def index(): 
    return {"message" : "Hola, Fast API. Esto es una funcion tipo Get"}
#funcion que se va a ejecutar

#parametros variables
@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}

# levanta el servidor: uvicorn main:app --reload
# Entornos virtuales: https://docs.python.org/es/3/tutorial/venv.html
# Installation: https://fastapi.tiangolo.com/#installation
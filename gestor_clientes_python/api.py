from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse 
import database as db
from pydantic import BaseModel, constr, validator
import helpers


# SE creara una nueva clase modelo 


class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3) # type: ignore
    nombre:constr(min_length=2, max_length=30) # type: ignore
    apellidos:constr(min_length=2, max_length=30) # type: ignore



class ModeloCrearCliente(ModeloCliente):
    @validator('dni')
    def validar_dni(cls,dni):
        if helpers.dni_valido(dni,db.Clientes.lista):
            return dni 
        raise ValueError("Cliente ya existente o dni incorrecto")

  

headers = {"Content-Type": "application/json; charset=utf-8"}

app= FastAPI(
    title="API del Gestor de clientes",
    description="Ofrece diferentes operaciones para gestionar a los clientes en la base de datos."
)


# Devolverá la lista de clientes 

@app.get('/clientes/', tags=["Clientes"])
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)



# Buscar un cliente a partir del DNI 


@app.get('/clientes/recuperar/{dni}',tags=["Clientes"])
async def clientes_buscar(dni:str): 
    cliente = db.Clientes.buscar(dni=dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict(), headers=headers)


# Ruta para crear clientes 
# Hay que crear uan instancia de un lciente a psrtir de uan info y devolver ese cliente en forma JSON 

@app.post('/clientes/crear',tags=["Clientes"])
async def clientes_crear(datos: ModeloCrearCliente):

    cliente= db.Clientes.crear(datos.dni, datos.nombre, datos.apellidos)
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no encontrado")



# Ruta para modificar clientes 

@app.put('/clientes/actualizar',tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):

    if db.Clientes.buscar(datos.dni):
        cliente= db.Clientes.crear(datos.dni, datos.nombre, datos.apellidos)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# Ruta para eliminar a los clientes 
@app.delete('/clientes/borrar/{dni}',tags=["Clientes"])
async def clientes_borrar(dni:str):
    if db.Clientes.buscar(dni):
        cliente= db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="Cliente no encontrado")





print("Servidor de la API...")
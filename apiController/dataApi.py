from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list=[]

class shipping(BaseModel):
    origen:str
    cedula:int
    nombres:str
    apellidos:str
    telefono:int
    destino:str
    cedulaDestino:int
    nombresDestino:str
    apellidosDestino:str
    telefonoDestino:int
    direccion:str
    indicaciones:str
    estado:str

@app.get("/viewShipping")
def view():
    return list

@app.post("/addShipping")
def save(data:shipping):
    list.append(data)
    return{"Response ":"Saved data"}

@app.put("/updateShipping")
def update(data:shipping):
    status=False
    for item in list:
        if item.cedula == data.cedula:
            list.remove(item)
            list.append(data)
            status=True
            break
    
    return{"Response ":"updated data"}

@app.delete("/deleteShipping")
def delete(cedula:int):
    status=False
    for item in list:
        if item.cedula == cedula:
            list.remove(item)
            status=True
            break
    if status==True:
        return{"Response ":"Deleated data"}
    else:
        return{"Response ":"data not found"}
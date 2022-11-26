from fastapi import FastAPI
from pydantic import BaseModel
from models import shipping_db
from mongoengine import connect

import json

connect(db="fastData_data_base", host="localhost", port=27017)

app = FastAPI()

#list=[]

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

    shippingInfo = shipping_db.objects.to_json()
    return json.loads(shippingInfo)
    

@app.post("/addShipping")
def saving(data:shipping):
    temporary=shipping_db()
    temporary.origen=data.origen
    temporary.cedula=data.cedula
    temporary.nombres=data.nombres
    temporary.apellidos=data.apellidos
    temporary.telefono=data.telefono
    temporary.destino=data.destino
    temporary.cedulaDestino=data.cedulaDestino
    temporary.nombresDestino=data.nombresDestino
    temporary.apellidosDestino=data.apellidosDestino
    temporary.telefonoDestino=data.telefonoDestino
    temporary.direccion=data.direccion
    temporary.indicaciones=data.indicaciones
    temporary.estado=data.estado
    temporary.save()
    
    shippingInfo = shipping_db.objects().to_json()
    return json.loads(shippingInfo)


@app.put("/updateShipping")
def update(data:shipping):
    status=False
    for item in list:
        if item.cedula == data.cedula:
            list.remove(item)
            list.append(data)
            status=True
            break
    if status==True:
        return{"Response ":"updated data"}
    else:
        return{"Response ":"data not found"}

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
        return{"Response ":"Data not found"}
from fastapi import FastAPI
from pydantic import BaseModel
from models import shipping_db
from mongoengine import connect

#from datetime import date
from datetime import datetime

import json

connect(db="fastData_data_base", host="localhost", port=27017)

app = FastAPI()

#list=[]

class shipping(BaseModel):
    guia:int
    origen:str
    cedula:int
    nombres:str
    apellidos:str
    telefono:int
    direccion:str
    indicaciones:str
    destino:str
    cedulaDestino:int
    nombresDestino:str
    apellidosDestino:str
    telefonoDestino:int
    direccionDestino:str
    indicacionesDestino:str
    estado:str

@app.get("/viewShipping")
def view():

    shippingInfo = shipping_db.objects.to_json()
    return json.loads(shippingInfo)
    
    

@app.post("/addShipping")
def saving(data:shipping):

    now = datetime.now()
    temporary=shipping_db()
    temporary.guia=data.guia=int(now.strftime("%Y%m%d%H%M%S"))
    temporary.origen=data.origen.upper()
    temporary.cedula=data.cedula
    temporary.nombres=data.nombres.upper()
    temporary.apellidos=data.apellidos.upper()
    temporary.telefono=data.telefono
    temporary.direccion=data.direccion.upper()
    temporary.indicaciones=data.indicaciones.upper()
    temporary.destino=data.destino.upper()
    temporary.cedulaDestino=data.cedulaDestino
    temporary.nombresDestino=data.nombresDestino.upper()
    temporary.apellidosDestino=data.apellidosDestino.upper()
    temporary.telefonoDestino=data.telefonoDestino
    temporary.direccionDestino=data.direccionDestino.upper()
    temporary.indicacionesDestino=data.indicacionesDestino.upper()
    temporary.estado=data.estado.upper()
    temporary.save()
    
    shippingInfo = shipping_db.objects().to_json()
    return json.loads(shippingInfo)


@app.put("/updateShipping")
def update(data:shipping):

    shipping_db.objects(guia=data.guia).update_one(telefono=data.telefono, telefonoDestino=data.telefonoDestino, direccion=data.direccion.upper(), direccionDestino=data.direccionDestino.upper(), indicaciones=data.indicaciones.upper(), indicacionesDestino=data.indicacionesDestino.upper(), estado=data.estado.upper())


@app.delete("/deleteShipping")
def delete(guia:int):
    shipping_db.objects(guia=guia).delete()
    return {"Mensaje": "Eliminado"}

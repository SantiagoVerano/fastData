from mongoengine import Document,StringField,IntField

class shipping_db(Document):
    guia=IntField()
    origen=StringField()
    cedula=IntField()
    nombres=StringField()
    apellidos=StringField()
    telefono=IntField()
    destino=StringField()
    cedulaDestino=IntField()
    nombresDestino=StringField()
    apellidosDestino=StringField()
    telefonoDestino=IntField()
    direccion=StringField()
    indicaciones=StringField()
    estado=StringField()

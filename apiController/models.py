from mongoengine import Document,StringField,IntField

class shipping_db(Document):
    guia=IntField()
    origen=StringField()
    cedula=IntField()
    nombres=StringField()
    apellidos=StringField()
    telefono=IntField()
    direccion=StringField()
    indicaciones=StringField()
    destino=StringField()
    cedulaDestino=IntField()
    nombresDestino=StringField()
    apellidosDestino=StringField()
    telefonoDestino=IntField()
    direccionDestino=StringField()
    indicacionesDestino=StringField()
    estado=StringField()

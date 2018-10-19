from App import db
from werkzeug.security import generate_password_hash,check_password_hash

class Registro(db.Model):
   
    id=db.Column(db.Integer,primary_key=True)
    Nombre=db.Column(db.String(20),nullable=False)
    Email=db.Column(db.String(20),nullable=False)
    contrasena=db.Column(db.String(100),nullable=False)

    def __init__(self,Nombre,Email,contrasena):
        self.Nombre=Nombre
        self.Email=Email
        self.contrasena=self.__genera_contra(contrasena)

    def __genera_contra(self,contrasena):
        return generate_password_hash(contrasena)

    def retun_contra(self,contrasena):
        return check_password_hash(self.contrasena,contrasena)
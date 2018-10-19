from App import db

class Proveedor(db.Model):
    __tablename__='proveedor'
    id=db.Column(db.Integer,primary_key=True)
    razonSolcial=db.Column(db.String(20),nullable=False)
    CI = db.Column(db.String(10))
    Direccion = db.Column(db.String(50))
    Correo = db.Column(db.String(30))
    convencional= db.Column(db.String(10))
    Celular= db.Column(db.String(10))
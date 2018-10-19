from App import db

class ingreso(db.Model):
    __tablename__='Ingreso'
    cod_ingreso=db.Column(db.Integer,primary_key=True)
    fecha_ingreso=db.Column(db.DateTime)
    Receptor=db.Column(db.String(12),nullable=False)
    Emisor=db.Column(db.String(12),nullable=False)
    fkproveedor=db.Column(db.Integer,db.ForeignKey('proveedor.id'),nullable=False)
    #fk_proveedor=db.relationship('proveedor',backref=db.backref('Ingreso'),lazy=True)

class Salida (db.Model):
    __tablename__='salida'
    Codigo= db.Column(db.Integer,primary_key=True)
    fecha_Salida=db.Column(db.DateTime,nullable=True)
    Receptor=db.Column(db.String(20),nullable=True)

class Detalle(db.Model):
    __tablename__='Detalle'
    id=db.Column(db.Integer(),primary_key=True)
    codProducto=db.Column(db.Integer, db.ForeignKey('Productos.Codigo'), nullable=False)
    codingreso=db.Column(db.Integer, db.ForeignKey('Ingreso.cod_ingreso'))
    codsalida=db.Column(db.Integer, db.ForeignKey('salida.Codigo') )
    cantidad=db.Column(db.Integer, nullable=False)
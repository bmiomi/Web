from App import db

class ingreso(db.Model):
    __tablename__='Ingreso'
    cod_ingreso=db.Column(db.Integer,primary_key=True)
    fecha_ingreso=db.Column(db.Date)
    Receptor=db.Column(db.String(12),nullable=False)
    Emisor=db.Column(db.String(12),nullable=False)
    fkproveedor=db.Column(db.Integer,db.ForeignKey('proveedor.id'),nullable=False)
    #Relacion
    fk_proveedor=db.relationship('Proveedor', cascade="all,delete")


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
    Docenas=db.Column(db.Integer, nullable=False)
    Unidades=db.Column(db.Integer, nullable=False)
#relaciones
    fk_producto=db.relationship("productos")
    fk_Ingreso=db.relationship("ingreso")
    fk_Salida=db.relationship("Salida")
    
#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Proveedor(db.Model):
    __tablename__='proveedor'
    id=db.Column(db.Integer,primary_key=True)
    razonSolcial=db.Column(db.String(20),nullable=False)
    CI = db.Column(db.String(10))
    Nombre = db.Column(db.String(20))
    Apellido = db.Column(db.String(20)) 
    FechaNacimiento = db.Column(db.DateTime)
    Sexo = db.Column(db.String(1))

class Clientes(db.Model):
    __tablename__ = "Cliente"
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Apellido = db.Column(db.String(50))

    def as_dict(self):
        dic={'Id': self.id,
        'Nombre': self.Nombre,
        'Apellido': self.Apellido,
        'FechaNacimiento': self.FechaNacimiento
        }
        return dic

class productos(db.Model):
    __tablename__='Productos'
    Codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    Precio = db.Column(db.Numeric)
    stock = db.Column(db.Numeric)
    Categoria= db.Column(db.Integer,db.ForeignKey("categoria.id"),nullable=False)
    categori=db.relationship('Categoria', backref=db.backref('Productos',lazy=True))

class Categoria(db.Model):
    __tablename__='categoria'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Nombre = db.Column(db.String(15), nullable=False)
    
class ingreso(db.Model):
    __tablename__='Ingreso'
    cod_ingreso=db.Column(db.Integer,primary_key=True)
    fecha_ingreso=db.Column(db.DateTime)
    Receptor=db.Column(db.String(12),nullable=False)
    Emisor=db.Column(db.String(12),nullable=False)
    fkproveedor=db.Column(db.Integer,db.ForeignKey('proveedor.id'),nullable=False)
    #fk_proveedor=db.relationship('proveedor',backref=db.backref('Ingreso'))

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

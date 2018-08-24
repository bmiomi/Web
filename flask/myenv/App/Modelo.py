#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() 

class Proveedor(db.Model):
	id=db.column(db.Integer)
	CI= db.Column(db.String(10),primary_key=True)
	Nombre=db.Column(db.String(20))
	Apellido=db.Column(db.String(20))
	FechaNacimiento=db.Column(db.DateTime)
	Sexo=db.Column(db.String(1))

	def as_dict(self):
		return {'CI': self.CI}

class Clientes(db.Model):
	__tablename__= "Cliente"
	id = db.Column(db.Integer, primary_key=True)
	Nombre = db.Column(db.String(50))
	Apellido= db.Column(db.String(50))
	estado=db.column(db.String(20))
	FechaNacimiento=db.Column(db.String(50))
	Sexo=db.column=(db.String(1))

class productos(db.Model):
	__tablename__= "Productos"
	Codigo = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50),nullable=False)
	Categoria = db.Column(db.String(50),nullable=False)
	Precio =db.Column(db.Integer)
	stock =db.Column(db.Integer)
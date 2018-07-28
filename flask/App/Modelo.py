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



"""
class Registro(db.Model):
	__tablename__= "Logins"
	id = db.Column(db.Integer, primary_key=True)
	usuario = db.Column(db.String(50),nullable=False)
	contrasena= db.Column(db.String(50),nullable=False)
	EMAIL=db.Column(db.String(50),nullable=False)



class Accion(db.Model):
	__tablename__= "Acciones"
	id = db.Column(db.Integer, primary_key=True)
	Deporte = db.Column(db.String(50),nullable=False)
	Estudio= db.Column(db.String(50),nullable=False)
	fk_usuario=db.Column(db.Integer,db.ForeignKey('Logins.id'))

"""
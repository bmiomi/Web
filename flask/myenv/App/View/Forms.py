#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,PasswordField,SelectField,RadioField,IntegerField
from wtforms.fields.html5 import DateField

class Fr_Proveedor(Form):

	CI = StringField('CI',[validators.Required(message="La CI es Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio inserta una CI valida')])
	Nombre = StringField('Nombre',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Nombre valido")])
	Apellido = StringField('Apellido',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Apellido valido" )])
	FechaNacimiento = DateField('FechaNacimiento')
	Sexo = RadioField('Sexo', [validators.DataRequired()], choices=[('M','Masculino'),('F','Femenino')])

def validardatos(form,field):
	if len(field.data)>0:
		raise validators.ValidationError ("error")
	

class Fr_Personal (Form):
			
	id=StringField('CI',[validators.Required(message="la CI es Obligatorio"),validators.Length(min=4,max=10,message="El campo es obligatorio")])
	Nombre=StringField('Nombre')
	Apellido=StringField('Apellido')
	Estado=RadioField('Estado' ,choices=[('Soltero','Soltero'),('Casado','Casado'),('Divorsiado','Divorciado'),('Union Libre','Union Libre')])
	FechaNacimiento=DateField('FechaNacimiento')


class Fr_Productos(Form):
		
	Codigo= IntegerField('Codigo',[validators.Required(message="El codigo del producto es Obligatorio")])
	nombre=StringField('Nombre')
	Categoria=SelectField('Categoria',[validators.Required(message="Seleccione un producto es obligatorio")],choices =[('Legumbres','Espinaca'),('Fruta','manzana')])
	Precio=IntegerField('Precio')
	stock=IntegerField('Stock')

class Fr_Categoria(Form):
	Codigo=StringField('Codigo')
	Nombre=StringField('Nombre Identificativo')


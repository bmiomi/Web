#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,PasswordField,RadioField,IntegerField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from Modelos.Modelo import Categoria,Proveedor,productos


def validardatos(form,field):
	if len(field.data)>0:
		raise validators.ValidationError ("error")


class Fr_Proveedor(Form):

	RasonSocial = StringField('Rason Social',[validators.Required(message="Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio')])
	CI = StringField('Identificasion',[validators.Required(message="La CI es Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio inserta una CI valida')])
	Nombre = StringField('Nombre',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Nombre valido")])
	Apellido = StringField('Apellido',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Apellido valido" )])
	FechaNacimiento = DateField('FechaNacimiento')
	Sexo = RadioField('Sexo', [validators.DataRequired()], choices=[('M','Masculino'),('F','Femenino')])	

class Fr_Personal (Form):
			
	id=StringField('CI',[validators.Required(message="la CI es Obligatorio"),validators.Length(min=4,max=10,message="El campo es obligatorio")])
	Nombre=StringField('Nombre')
	Apellido=StringField('Apellido')

def get_Categoria():
    return Categoria.query
class Fr_Productos(Form):
		
	Codigo= IntegerField('Codigo',[validators.Required(message="El codigo del producto es Obligatorio")])
	nombre=StringField('Nombre')
	Categoria=QuerySelectField(label="Categoria",
							   query_factory=get_Categoria,
                               get_label="Nombre",
							   allow_blank=True,
							   blank_text="Selecccionar."
							   )
	Precio=IntegerField('Precio')
	stock=IntegerField('Stock')

class Fr_Categoria(Form):

	Codigo=StringField('Codigo')
	Nombre=StringField('Nombre Identificativo')


def get_proveedor():
	return Proveedor.query
def get_producto():
	return productos.query

class Fr_Almacen(Form):
		
	Codigo= IntegerField('Codigo',[validators.Required(message="El codigo del producto es Obligatorio")])
	nombre=QuerySelectField('Producto',allow_blank=True,blank_text='Seleccionar',query_factory=get_producto,get_label='nombre')
	fecha=DateField("FECHA")
	Receptor=StringField('Receptor')
	proveedor=QuerySelectField('Proveedor',allow_blank=True,blank_text='Seleccionar',query_factory=get_proveedor,get_label='razonSolcial')
	Emisor=StringField('Emisor')
	cantidad=IntegerField('Cantidad')

class Fr_SalidaAlmacen(Form):
		
	Codigo= IntegerField('Codigo',[validators.Required(message="El codigo del producto es Obligatorio")])
	nombre=QuerySelectField('Producto',allow_blank=True,blank_text='Seleccionar',query_factory=get_producto,get_label='nombre')
	fecha=DateField("FECHA")
	Receptor=StringField('Receptor')
	cantidad=IntegerField('Cantidad')

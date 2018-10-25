#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,IntegerField,HiddenField
from wtforms.fields.html5 import EmailField

class Fr_Proveedor(Form):
	
	
	RasonSocial = StringField('Rason Social',[validators.Required(message="Obligratorio"),
											  validators.Length(min=4,max=10,message='No contiene cantidad de caracteres validos')])
	
	CI = IntegerField('Identificasion',[validators.InputRequired(message="La CI es Obligratorio")])
	
	Direccion = StringField('Direccion',[validators.InputRequired(message="Llene el campo con la Direccion")])
	
	Correo = EmailField('Correo', [validators.DataRequired()])	
	
	Convencional= IntegerField('Convencional', [validators.DataRequired()])	
	
	Celular= IntegerField('Celular', [validators.DataRequired()])

	
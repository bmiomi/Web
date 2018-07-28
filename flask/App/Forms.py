#!/usr/bin/python
# -*- coding: utf-8 -*-

from wtforms import Form 
from wtforms import BooleanField,validators,StringField,PasswordField
from wtforms.fields.html5 import DateField

class Proveedor(Form):

	CI = StringField('CI',[validators.Required(message="La CI es Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio inserta una CI valida')])
	
	Nombre = StringField('Nombre',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Nombre valido")])
	Apellido = StringField('Apellido',[validators.Length(min=4,max=20,message="El campo es Obligatorio inserta un Apellido valido" )])
	FechaNacimiento = DateField('FechaNacimiento')
	Sexo = BooleanField('Sexo', [validators.DataRequired()])




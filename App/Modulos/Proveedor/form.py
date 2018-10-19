#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,IntegerField


class Fr_Proveedor(Form):

	RasonSocial = StringField('Rason Social',[validators.Required(message="Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio')])
	CI = StringField('Identificasion',[validators.Required(message="La CI es Obligratorio"),validators.Length(min=4,max=10,message='El campo es Obligatorio inserta una CI valida')])
	Direccion = StringField('Direccion')
	Correo = StringField('Correo', [validators.DataRequired()])	
	Convencional= StringField('Convencional', [validators.DataRequired()])	
	Celular= StringField('Celular', [validators.DataRequired()])
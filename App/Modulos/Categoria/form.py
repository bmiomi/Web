#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form ,validators,StringField


def pp(form,field):
	if len(field.data)==0:
		raise validators.ValidationError('dsdas')

class Fr_Categoria(Form):

	Codigo=StringField('Codigo')
	Nombre=StringField('Nombre Identificativo',[validators.length(min=3,max=6,message="error0")])

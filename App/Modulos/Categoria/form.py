#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form ,validators,StringField
from wtforms.validators import ValidationError
from App.Modulos.Categoria.model import Categoria
from App.Validadores.validar import Unique
    
class Fr_Categoria(Form):

	Codigo=StringField('Codigo')
	Nombre=StringField('Nombre Identificativo',[
                        validators.Length(min=2,message="No exede o exede la cantidad de caracteres validos"),
                        Unique(Categoria,Categoria.Nombre)])

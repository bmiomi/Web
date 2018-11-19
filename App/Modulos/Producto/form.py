#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,PasswordField,RadioField,IntegerField,SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from App.Modulos.Categoria.model import Categoria
from App.Modulos.Producto.model import productos
from App.Validadores.validar import Unique

def get_Categoria():
    return Categoria.query

def codigos():
    d=productos.query.order_by(productos.Codigo.desc()).first()    

    if d is None:
        data=1
    else:
        data=d.Codigo+1
    return data 

class Fr_Productos(Form):
    Codigo= IntegerField('Codigo',[validators.Required(message="El codigo del producto es Obligatorio")],default=codigos)
    nombre=StringField('Modelo',[Unique(productos,productos.nombre)])
    Categoria=QuerySelectField(label="Categoria",query_factory=get_Categoria,
                               get_label="Nombre",
			       allow_blank=True,
			       blank_text="Selecccionar.")
    P_U_C=IntegerField('P.U.C')
    P_U_V=IntegerField('P.U.V')
    #stock=IntegerField('Stock')


"""
bulto <100dc 
por mayor = 12dc 
cuarto > 12dc
unidad=1
"""
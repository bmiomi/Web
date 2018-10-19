#!/usr/bin/python
# -*- coding: utf-8 -*-
from wtforms import Form 
from wtforms import validators,StringField,IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField
from App.Modulos.Proveedor.model import Proveedor
from App.Modulos.Producto.model import productos
from App.Modulos.Almacen.model import ingreso,Salida
from datetime import datetime
def get_proveedor():
	return Proveedor.query

def get_producto():
	return productos.query

def data():
    data=ingreso.query.order_by(ingreso.cod_ingreso.desc()).first() 
    if data is None:
        return 1
    else:
        return data.cod_ingreso+1

class Fr_Almacen(Form):
    Codigo= IntegerField('Ingreso N#',[validators.Required(message="El codigo del producto es Obligatorio")],default=data)
    nombre=QuerySelectField('Producto',allow_blank=True,blank_text='Seleccionar',query_factory=get_producto,get_label='nombre')
    fecha=DateField("FECHA",default=datetime.today)
    Receptor=StringField('Receptor')
    proveedor=QuerySelectField('Proveedor',allow_blank=True,blank_text='Seleccionar',query_factory=get_proveedor,get_label='razonSolcial')
    Emisor=StringField('Emisor')
    cantidad=IntegerField('Cantidad')

def datas():
    data=Salida.query.order_by(Salida.Codigo.desc()).first() 
    if data is None:
        return 1
    else:
        return data.Codigo+1

class Fr_SalidaAlmacen(Form):
    Codigo= IntegerField('Salida  N#',[validators.Required(message="El codigo del producto es Obligatorio")],default=datas)
    nombre=QuerySelectField('Producto',allow_blank=True,blank_text='Seleccionar',query_factory=get_producto,get_label='nombre')
    fecha=DateField("FECHA",default=datetime.today)
    Receptor=StringField('Receptor')
    cantidad=IntegerField('Cantidad')
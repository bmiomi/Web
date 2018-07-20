#!/usr/bin/python
# -*- coding: utf-8 -*-

from wtforms import Form ,StringField,PasswordField,validators,BooleanField

class F_Registro(Form):

	Usuario = StringField('Usuario',[ validators.Length(min=4, max=30,message='El campo debe contener un almenos 4 caracteres')])
	email = StringField('email', [ validators.length(min=10,max=30,message="Debe registrar el campo de  correo Electronico") ])
	contrasena=  PasswordField('Contraseña', [ validators.DataRequired()])
	confpassword = PasswordField('confirmar Contraseña')
	accept_tos = BooleanField('rename me', [validators.DataRequired()])

class F_login(Form):
	Usuario = StringField('Usuario', [validators.Length(min=4, max=30,message= 'El campo debe contener un almenos 4 caracteres' )])
	contrasena=  PasswordField('Contrasena', [ validators.DataRequired()])

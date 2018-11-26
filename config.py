#!/usr/bin/python
# -*- coding: utf-8 -*-
#basedtos://usuario:passsword@direccion/nombre base datos
import os
class Config(object):
	SECRET_KEY= 'miomi'

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 	"mysql://root:Rous@localhost/SQLALchemy"
	SQLALCHEMY_ECHO=True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	TRAP_BAD_REQUEST_ERRORS = True
#SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd ()) + "/flask1.db"	
	
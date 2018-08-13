#!/usr/bin/python
# -*- coding: utf-8 -*-
#basedtos://usuario:passsword@direccion/nombre base datos
class Config(object):

	SECRET_KEY= 'miomi'

class DevelopmentConfig(Config):
	
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 	"mysql://root:Rous@localhost/SQLAlchemy"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

#	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd ()) + "/flask.db"
#	SQLALCHEMY_DATABASE_URI = 	"mysql://root:Rous@localhost/SQLAlchemy"

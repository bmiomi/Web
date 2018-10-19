from wtforms import Form,validators,StringField,PasswordField,RadioField
from App.Modulos.varios.model import Registro

class Fr_login(Form):
    usuario=StringField('Email')
    contrasena=PasswordField('Password')

class Fr_register(Form):
    Nombre=StringField('Nombre',[validators.DataRequired()])
    Email=StringField('Email',[validators.DataRequired()])
    contrasena=PasswordField('Password',[validators.DataRequired()])
    pcontrasena=PasswordField('Password',[validators.DataRequired()])
    #check=RadioField('Acepta los Terminos')


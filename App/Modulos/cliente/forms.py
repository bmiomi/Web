from wtforms import Form 
from wtforms import validators,StringField

class Fr_Personal (Form):
    id=StringField('CI',[validators.Required(message="la CI es Obligatorio"),
    validators.Length(min=4,max=10,message="El campo es obligatorio")])
    Nombre=StringField('Nombre')
    Apellido=StringField('Apellido')
    
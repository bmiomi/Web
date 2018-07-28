#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,\
make_response,redirect,url_for,abort,session,escape,flash
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from config import DevelopmentConfig
from Modelo import Proveedor,db
import Forms

def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	return app

app=create_app()
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

#erro 404 paguina no encontrada
@app.errorhandler(404)
def page_not_found(e):
	return render_template("errores.html"),404

#raiz 
@app.route("/")
def index():
	title="Inicio"
	raiz=" Hola como estas Actualmente te encuentras en la raiz de la paguina "
	return  render_template("index.html",titulo=title,raiz=raiz)

#registro
@app.route("/register",methods=['GET','POST'])
def register():
	frm=Forms.F_Registro(request.form)
	if request.method == "POST" and frm.validate():
		if frm.contrasena.data == request.form["confpassword"]:			
			new_user= Registro(	
							usuario= frm.Usuario.data,
							contrasena=frm.contrasena.data,
							EMAIL=frm.email.data
							  )
			db.session.add(new_user)
			db.session.commit()
			return  redirect(url_for('Singup'))
		else:
			mensaje="Constrasena no coinciden"
			flash(mensaje)	
	return render_template("register.html",frm=frm)



#Inicio de Session
@app.route("/Singup")
def Singup():
	titulo="Singup"
#	frm = Forms.F_login(request.form)	
#	if request.method ==  "POST" and frm.validate():

#			user=frm.Usuario.data
#			mensaje= "Bienvenido {}".format (user)
#			flash(mensaje)
#			return render_template("index6.html")
#			response=make_response()
#			response.set_cookie('cookiess','cook')
	return render_template("Singup.html", titulo = titulo)



#Main
@app.route("/main")
def main():
	return  render_template("borrar/base.html")


@app.route("/proveedor",methods=['GET','POST'])
def proveedor():
#  intanciar el formularo 	
	frm=Forms.Proveedor(request.form)
# valiadar que el formulario envie los datos por el metodo post
	if request.method == 'POST':
		if frm.validate() and db.session.query(Proveedor.CI).filter_by(name = "0956235682").scalar() is not None:
#visualizar los datos en el Prompt
			print(frm.CI.data)
			print(frm.Nombre.data)
			print(frm.Apellido.data)
			print(frm.Sexo.data)
			print(frm.FechaNacimiento.data)		
	# obtener los datos del formulario		
			new_user= Proveedor(CI=frm.CI.data,
								Nombre=frm.Nombre.data,
								Apellido=frm.Apellido.data,
								FechaNacimiento=frm.FechaNacimiento.data,
								Sexo=frm.Sexo.data)
	#cargar los datos  a la sessin de la base datos
			db.session.add(new_user)
	# Insertar los datos en la base datos
			db.session.commit()
		else:
			print("error")
	return render_template("proveedor.html",frm=frm)


@app.route("/Cliente")
def Clientes():
	pass
	return render_template('cliente.html')


@app.route("/Lista") #lista sin conexion a base de datos.
def Lista():
	titulo = "Lista"

	listas=[

		{   
		    'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },

        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },

		 {
            'author': {'nickname': 'Marco'},
          
		    'body': 'The Avengers movie was so wonderfull!'
        },

		 {
            'author': {'nickname': 'carlos'},
            'body': 'The Avengers movie was so ugle!'
        }
	]
	print (listas)
	return render_template("lista.html", titulo=titulo ,listas=listas)

@app.route("/listadb")#lista con conexion a base de datos.
def listadb():
	return render_template("lista.html",listas=Proveedor.query.all())

#inicio
@app.route("/Inicio")
def Inicio():
	titulo = "Inicio"
	resivircookie=request.cookies.get('cookiess','default')
	print(resivircookie)
	return render_template("modal.html", titulo=titulo) 

if __name__ == "__main__":
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()# metodo para crear tablas y la propia db
	app.run( port=8000 )


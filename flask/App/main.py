#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template,request,make_response,redirect,url_for,abort,session,escape,flash
from werkzeug.security import generate_password_hash,check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from config import DevelopmentConfig
from Modelo import Proveedor,Clientes,productos,db
import Forms


def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	return app

app=create_app()
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)#erro 404 paguina no encontrada
def page_not_found(e):
	return render_template("errores.html"),404

@app.route("/") #raiz 
def index(): 	
	title="Inicio"
	raiz=" Hola como estas Actualmente te encuentras en la raiz de la paguina "
	return  render_template("index.html",titulo=title,raiz=raiz)

@app.route("/main") #Main
def main():
	return  render_template("borrar/base.html")

@app.route("/register",methods=['GET','POST']) #registro
def register():
	frm=Forms.F_Registro(request.form)
	if request.method == "POST" and frm.validate():
		if frm.contrasena.data == request.form["confpassword"]:			
			new_user= F_Registro(	
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

@app.route("/Singup") #Inicio de Session
def Singup():
	titulo="Singup"
	return render_template("Singup.html", titulo = titulo)

@app.route("/proveedor",methods=['GET','POST']) # registro de proveedor
def proveedor():
	frm=Forms.Fr_Proveedor(request.form)
	if request.method == 'POST' and frm.validate():
		print(frm.CI.data)
		print(frm.Nombre.data)
		print(frm.Apellido.data)
		print(frm.Sexo.data)
		print(frm.FechaNacimiento.data)		
		new_user= Proveedor(CI=frm.CI.data,
							Nombre=frm.Nombre.data,
							Apellido=frm.Apellido.data,
							FechaNacimiento=frm.FechaNacimiento.data,
							Sexo=frm.Sexo.data)
		db.session.add(new_user)
		db.session.commit()
	else:
		print("error")
	return render_template("frproveedor.html",frm=frm) 

@app.route("/listaP")#listado de Proveedores.
def listaP():
	pass
	return render_template("listaP.html",listas=Proveedor.query.all())

@app.route("/Cliente",methods=['GET','POST']) #registro de Clientes
def Cliente():
	frm=Forms.Fr_Clientes(request.form)
	return render_template('frcliente.html',frm=frm)

@app.route("/listaC") #listado de Clientes.
def listaC():
	titulo = "Listado de Clientes"
	return render_template("listaC.html", titulo=titulo ,listas=Clientes.query.all())

@app.route("/Productos",methods=['GET','POST']) #registro de Productos
def Productos():
	frm=Forms.Fr_Productos(request.form)
	if request.method == "POST" and frm.validate():
		pr=db.session.query(productos).filter_by(Codigo=frm.Codigo.data).first()
		print("este  producto ya existe ",str(pr))
		if pr is None:
#Insercion db
			dbproductos = productos (Codigo=frm.Codigo.data,nombre=frm.nombre.data,
									Categoria=frm.Categoria.data,Precio=frm.Precio.data,
									stock=frm.stock.data)
			db.session.add(dbproductos)
			db.session.commit()
		else:
			mensaje="Error al ingresar los datos esto de puede deber a que ya existe ese producto con ese codigo"
			flash(mensaje)
			print(mensaje)
	return render_template('frProductos.html',frm=frm)

@app.route("/listaPr") #listado de productos.	
def listaPr():
	titulo = "Listado de Productos"

	return render_template("listaPr.html", titulo=titulo,listas=productos.query.all())


if __name__ == "__main__":
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()# metodo para crear tablas y la propia db
	app.run( port=8000 )


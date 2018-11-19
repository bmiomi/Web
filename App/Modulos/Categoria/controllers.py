#Importacion de Dependencias Flask
from flask import Blueprint, Flask, render_template, request, redirect,url_for,flash
# Importacion de modulo de ModeloCliente
from App.Modulos.Categoria.model import Categoria
from App import db
#Inportacion de modulo de formularioCliente
from App.Modulos.Categoria import form

#
_Categoria=Blueprint('Categoria',__name__,url_prefix='/Categoria')


@_Categoria.route("/Categoria",methods=['POST', 'GET']) 
def categoria():
    frm = form.Fr_Categoria(request.form)
    if request.method == "POST" and frm.validate():
        pr = Categoria.query.filter_by(Nombre=request.form['Nombre']).first()
        print(request.form['Nombre'])
        if  pr is None:
            dbcategoria = Categoria(Nombre=request.form['Nombre'])
            db.session.add(dbcategoria)
            db.session.commit()
            flash("Los datos an sido exitosamente Guardados")
            return redirect(url_for('Categoria.ListaCate'))
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
    return render_template("Categoria/frCategoria.html", frm=frm)


@_Categoria.route("/ListaCate")
def ListaCate():
	page=request.args.get('page',1,type=int)
	list=Categoria.query.paginate(page=page,per_page=3)
	return render_template("Categoria/ListaCate.html", lista=list,imagens='Banana_icon.png')
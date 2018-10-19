#Importacion de Dependencias Flask
from flask import Blueprint, Flask, render_template, request, make_response, redirect,url_for,flash, jsonify
# Importacion de modulo de ModeloCliente
from App.Modulos.Categoria.model import Categoria
from App import db
#Inportacion de modulo de formularioCliente
from App.Modulos.Categoria import form

#
_Categoria=Blueprint('Categoria',__name__,url_prefix='/Categoria')


@_Categoria.route("/Categoria",methods=['POST', 'GET']) 
def categoria():
    frm = form.Fr_Categoria()
    if request.method == "POST":
        pr = Categoria.query.filter_by(Nombre=frm.Nombre.data).first()
            
        if frm.errors:
            dbcategoria = Categoria(
                Nombre=frm.Nombre.data
            )
#            db.session.add(dbcategoria)
 #           db.session.commit()
            flash("Los datos an sido exitosamente Guardados")
            return redirect(url_for('Categoria.categoria'))
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
            print(frm.errors)
    return render_template("Categoria/frCategoria.html", frm=frm)


@_Categoria.route("/ListaCate")
def ListaCate():
	page=request.args.get('page',1,type=int)
	list=Categoria.query.paginate(page=page,per_page=3)
	return render_template("Categoria/ListaCate.html", lista=list)
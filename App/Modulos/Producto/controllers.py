#Importacion de Dependencias Flask
from flask import Blueprint, Flask, render_template, request, make_response, redirect,url_for,flash, jsonify
from App import db
# Importacion de modulo de ModeloCliente
from App.Modulos.Producto.model import productos
#Inportacion de modulo de formularioCliente
from App.Modulos.Producto import form 
#
Producto=Blueprint('Productos',__name__,url_prefix='/Producto')

@Producto.route('/Productos', methods=['GET', 'POST'])  # registro de Productos
def Productos():
    frm = form.Fr_Productos(request.form)
    
    if request.method == 'POST':
        pr = productos.query.filter_by(Codigo=frm.Codigo.data).first()
        if frm.validate() and pr is None:
            dbproductos = productos(Codigo=frm.Codigo.data,
                                    nombre=frm.nombre.data,
                                    Precio=frm.Precio.data,
                                    stock=0,
                                    Categoria=request.form['Categoria']
                                    )
            db.session.add(dbproductos)
            db.session.commit() 
            flash("Los datos an sido exitosamente Guardados")
        else:
            flash("Error: No se registrado con exito sus Datos.")
    return render_template('Producto/frProductos.html', frm=frm)
    
@Producto.route("/listaPr")  # listado de productos.
def listaPr():
	titulo = "Listado de Productos"
	listas = productos.query.order_by(productos.Codigo).all()
	return render_template("Producto/listaPr.html", titulo=titulo, listas=listas)

@Producto.route("/UpdatePr", methods=['POST'])
def UpdatePr():

    update = productos.query.filter_by(id=request.form['Codigo']).first()
    update.Nombre = request.form['Nombre']
    update.Apellido = request.form['Categoria']
    update.FechaNacimiento = request.form['Precio']
    update.FechaNacimiento = request.form['stock']
    db.session.commit()
    return redirect(url_for('listaPr'))


@Producto.route('/deletePr/<string:id>')
def deletePr(id):
    dlete = productos.query.filter_by(codigo=id).delete()
    db.session.commit()
    return redirect(url_for('listaPr'))

@Producto.route("/modalPr")
def modalPr():
    frm = form.Fr_Productos(request.form)
    return render_template("modal/modalproducto.html", frm=frm, title="Producto")
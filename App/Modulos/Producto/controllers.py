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
                                    PrecioCompra=frm.P_U_C.data,
                                    PrecioVenta=frm.P_U_V.data,
                                    stock=0,
                                    Categoria=request.form['Categoria']
                                    )
            db.session.add(dbproductos)
            db.session.commit() 
            flash("Los datos an sido exitosamente Guardados")
            return redirect(url_for('Productos.Productos'))
        else:
            flash("Error: No se registrado con exito sus Datos.")
    return render_template('Producto/frProductos.html', frm=frm)
    
@Producto.route("/listaPr", methods=['GET','POST'])  # listado de productos.
def listaPr():
	titulo = "Listado de Productos"
	listas = productos.query.order_by(productos.Codigo).all()
	return render_template("Producto/listaPr.html", titulo=titulo, listas=listas)


@Producto.route("/UpdatePr", methods=['POST'])
def UpdatePr():
    update = productos.query.filter_by(Codigo=request.form['Codigo']).first()
    update.nombre = request.form['nombre']
    update.PrecioCompra = request.form['P_U_C']
    update.PrecioVenta = request.form['P_U_V']
    db.session.commit()
    return redirect(url_for('Productos.listaPr'))

@Producto.route('/deletePr',methods=['POST'])
def deletePr():
    print(request.form)
    dlete = productos.query.filter_by(Codigo=request.form['Codigo']).first()
    db.session.delete(dlete)
    db.session.commit()
    return redirect(url_for('Productos.listaPr'))

@Producto.route("/modalPr")
def modalPr():
    frm = form.Fr_Productos(request.form)
    return render_template("modal/modalproducto.html", frm=frm, title="Producto")
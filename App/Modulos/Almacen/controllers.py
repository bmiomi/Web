#Importacion de Dependencias Flask
from flask import Blueprint, Flask, render_template, request, make_response, redirect,url_for,flash, jsonify
#Importacion base datos
from App import app
# Importacion de modulo de ModeloCliente
from App.Modulos.Almacen.model import ingreso,Salida,Detalle
#Inportacion de modulo de formularioCliente
from App.Modulos.Almacen import form 
from App import db

Almacen=Blueprint('Almacen',__name__,url_prefix='/Almacen')

@Almacen.route('/IngresoAlmacen',methods=['GET','POST'])
def Ingreso():
    frm=form.Fr_Almacen()
    if request.method == 'POST':
        ca=ingreso.query.filter_by(cod_ingreso=request.form['Codigo']).first()
        cb=Detalle.query.filter_by(id=frm.Codigo.data).first()
        if ca is None and cb is None:
            dbingreso=ingreso(
                cod_ingreso=request.form['Codigo'],
                fecha_ingreso=request.form['fecha'],
                Receptor=request.form['Receptor'],
                Emisor=request.form['Emisor'],
                fkproveedor=request.form['proveedor']            )
            db.session.add(dbingreso)
            dbdetalle=Detalle(
                 codProducto=request.form['nombre'],
                 codingreso=request.form['Codigo'],
                 codsalida= None,
                 cantidad=request.form['cantidad']
                 )
            db.session.add(dbdetalle)
            print
            db.session.commit()
            flash("se ah registrado con exito sus Datos")
            return redirect(url_for('Almacen.Ingreso'))
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
    return render_template('Almacen/almacen.html',frm=frm)

@Almacen.route('/SalidaAlmacen',methods=['GET','POST'])
def SalidaAl():
    frm=form.Fr_SalidaAlmacen(request.form)
    return render_template("Almacen/SalidaAlmacen.html",frm=frm)

@Almacen.route('/MovimientosAlmacen')
def Movimientos():
    return 'Hola baby'


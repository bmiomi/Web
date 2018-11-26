#Importacion de Dependencias Flask
from flask import Blueprint, Flask, render_template, request, make_response, redirect,url_for,flash, jsonify
#Importacion base datos
from App import app
# Importacion de modulo de ModeloCliente
from App.Modulos.Almacen.model import ingreso,Salida,Detalle
from App.Modulos.Categoria.model import Categoria

from App.Modulos.Producto.model import productos
from App.Modulos.Proveedor.model import Proveedor
from sqlalchemy import func, and_,between
#Inportacion de modulo de formularioCliente
from App.Modulos.Almacen import form 
from App import db

Almacen=Blueprint('Almacen',__name__,url_prefix='/Almacen')

@Almacen.route('/IngresoAlmacen',methods=['GET','POST'])
def Ingreso():
    frm=form.Fr_Almacen()
    print(request.form)
    if request.method == 'POST':
        ca=ingreso.query.filter_by(cod_ingreso=request.form['Codigo']).first()
        if ca is None:
            dbingreso=ingreso(
                cod_ingreso=request.form['Codigo'],
                fecha_ingreso=request.form['fecha'],
                Receptor=request.form['Receptor'],
                Emisor=request.form['Emisor'],
                fkproveedor=request.form['proveedor'])

            dbdetalle=Detalle(
                 codProducto=request.form['Producto'],
                 codingreso=request.form['Codigo'],
                 codsalida= None,
                 Docenas=request.form['Docenas'],
                 Unidades=0
                 )

            db.session.add(dbingreso)
            db.session.add(dbdetalle)
            db.session.commit()
            flash("se ah registrado con exito sus Datos")
            return redirect(url_for('Almacen.Ingreso'))
        else:
            flash("Error: No se ah registrado con exito sus Datos")
    return render_template('Almacen/almacen.html',frm=frm)

@Almacen.route('/SalidaAlmacen',methods=['GET','POST'])
def SalidaAl():
    frm=form.Fr_SalidaAlmacen()
   
    if request.method == 'POST':
        ca=Salida.query.filter_by(Codigo=request.form['Codigo']).first()
        if ca is None:
            dbSALIDA=Salida(
                Codigo=request.form['Codigo'],
                fecha_Salida=request.form['fecha'],
                Receptor=request.form['Receptor']
                )
            dbdetalle=Detalle(
                 codProducto=request.form['nombre'],
                 codingreso=None,
                 codsalida= request.form['Codigo'],
                 Docenas=request.form['cantidad'],
                 Unidades=0
                 )
            db.session.add(dbSALIDA)
            db.session.add(dbdetalle)
            db.session.commit()
            flash("se ah registrado con exito sus Datos")
            return redirect(url_for('Almacen.SalidaAl'))
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
    return render_template("Almacen/SalidaAlmacen.html",frm=frm)



@Almacen.route('/MovimientosAlmacen')
def Movimientos():
    sql= db.session.query(Categoria.Nombre,productos.nombre,ingreso.fecha_ingreso,func.count(Detalle.codingreso)
    ).filter(Categoria.id== productos.Categoria 
    ).filter( productos.Codigo == Detalle.codProducto
    ).filter(  Detalle.codingreso==ingreso.cod_ingreso
    ).filter(ingreso.fecha_ingreso == '2018-11-25'
    ).group_by(productos.nombre)
    print(sql)


    detalle=sql
    return render_template('Almacen/Movimientos.html',detalle=detalle)


@Almacen.route('/modalAl')
def modalAL():
    sql="select fecha_ingreso from ingreso inner join detalle on codingreso=cod_ingreso where codProducto=2;"
    datos=db.session.execute(sql)
    return render_template('modal/modalalmacen.html',datos=datos)

@Almacen.route('/Inventa')
def Inventa():
    return render_template('Almacen/Inventa.html')
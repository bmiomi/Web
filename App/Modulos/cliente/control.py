#Importacion de Dependencias Flask
from flask import Blueprint,Flask, render_template, request, redirect,url_for,flash, jsonify
#importacion de Modulo basedatos
from App import db
# Importacion de modulo de ModeloCliente
from App.Modulos.cliente.models import Clientes
#Inportacion de modulo de formularioCliente
from App.Modulos.cliente import forms

cliente=Blueprint('Cliente',__name__,url_prefix='/Cliente')

@cliente.route("/Cliente/", methods=['GET', 'POST']) #Registro de Clientes
def Cliente():
    frm = forms.Fr_Personal(request.form)
    if request.method == 'POST':
        pr = Clientes.query.filter_by(id=request.form['id']).first()
        if frm.validate() and pr is None:
            cliente = Clientes(
                id=frm.id.data,
                Nombre=frm.Nombre.data,
                Apellido=frm.Apellido.data,
                FechaNacimiento=frm.FechaNacimiento.data
            )
            db.session.add(cliente)
            db.session.commit()
            flash("Se Aguardado los datos exitosamente")
        else:
            flash("Error:No se ha registrado con exito sus Datos.")
    return render_template('Cliente/frcliente.html', frm=frm)

@cliente.route("/listaC/") #Listado de Clientes.
def listaC():
    titulo = "Listado de Clientes"
    res = Clientes.query.all()
    return render_template("Cliente/listaC.html", titulos=titulo, res=res)

@cliente.route("/Update/", methods=['POST']) #Actualizacion de Cliente
def Update():
    update = db.session.query(Clientes).filter_by(
        id=request.form['id']).first()
    update.Nombre = request.form['Nombre']
    update.Apellido = request.form['Apellido']
    update.FechaNacimiento = request.form['FechaNacimiento']
    db.session.commit()
    return redirect(url_for('listaC'))

@cliente.route('/delete/<string:id>') #Eliminacion de Cliente
def delete(id):
    dlete = db.session.query(Clientes).filter_by(id=id).delete()
    print(dlete)
    db.session.commit()
    return redirect(url_for('listaC'))

@cliente.route("/Lp")  # jsonlistacliente
def Lp():
    res = Clientes.query.all()
    listaproveedores = [r.as_dict() for r in res]
    return jsonify({'data': listaproveedores})

@cliente.route("/modalc")
def modalc():
    form = forms.Fr_Personal()
    return render_template("modalcliente.html", frm=form, title="Cliente")
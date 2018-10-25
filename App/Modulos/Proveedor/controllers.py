#Importacion de Dependencias Flask
from flask import Blueprint,Flask, render_template, request,redirect,url_for,flash
#modelado de basedato.
from App import db
# Importacion de modulo de ModeloCliente
from App.Modulos.Proveedor.model import Proveedor
#Inportacion de modulo de formularioCliente
from App.Modulos.Proveedor import form

_Proveedor=Blueprint('Proveedor',__name__,url_prefix='/Proveedor')

@_Proveedor.route('/Proveedor', methods=['GET', 'POST'])  # registro de proveedor
def proveedor():
    frm = form.Fr_Proveedor(request.form)
    if request.method == 'POST':
        pr = Proveedor.query.filter_by(CI=frm.CI.data).first()
        if frm.validate() and pr is None:
            new_user = Proveedor(razonSolcial=frm.RasonSocial.data,
                                 CI=frm.CI.data,
                                 Direccion=frm.Direccion.data,
                                 Correo=frm.Correo.data,
                                 convencional=frm.Convencional.data,
                                 Celular=frm.Celular.data
                                )
            db.session.add(new_user)
            db.session.commit()
            flash("Se registrado con exito sus datos")
            return redirect(url_for('Proveedor.proveedor'))
        else:
            flash("Error: No se registrado con exito sus Datos")
    return render_template('Proveedor/frproveedor.html', frm=frm)

@_Proveedor.route('/listaP',methods=['POST','GET'])  # listado de Proveedores.
def listaP():
    titulo = "Lista Proveedor"
    return render_template("Proveedor/listaP.html", titulo=titulo, listas=Proveedor.query.all())

@_Proveedor.route('/UpdateP',methods=['POST','GET'])
def UpdateP():
    if request.method =='POST':
        updateP = Proveedor.query.filter_by(CI=request.form['CI']).first()
        print("proveedor con cedular: {0}"%(updateP))
        updateP.RasonSocial = request.form['RasonSocial']
        updateP.Direccion = request.form['Direccion']
        updateP.Correo = request.form['Correo']
        updateP.convencional= request.form['Convencional']
        updateP.Celular = request.form['Celuar']
        db.session.commit()
    return redirect(url_for('Proveedor.listaP'))


@_Proveedor.route('/deleteP/<string:id>',methods=['GET','POST'])
def deleteP(id=None):
    dlTP = Proveedor.query.filter_by(CI=id).first()
    print(dlTP)
    db.session.delete(dlTP) 
    db.session.commit()
    return redirect(url_for('Proveedor.listaP'))

@_Proveedor.route("/modalP")
def modalP():
    frm = form.Fr_Proveedor(request.form)
    return render_template("modal/modaproveedor.html", frm=frm, title="Proveedor")


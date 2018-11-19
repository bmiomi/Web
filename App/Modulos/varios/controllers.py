from flask import render_template,flash,request,Blueprint,redirect,url_for
from App import db
from App.Modulos.varios import forms
from App.Modulos.varios.model import Registro
from flask import session

varios=Blueprint('varios',__name__,url_prefix='/varios')



@varios.route('/register/', methods=['GET', 'POST'])  # registro
def register():
    frm=forms.Fr_register(request.form)
    if request.method == 'POST':
        nuevo_user = Registro(frm.Nombre.data,frm.Email.data,frm.contrasena.data)
        db.session.add(nuevo_user)
        db.session.commit()
        return redirect(url_for('varios.main'))
    else:
        mensaje = "Constrasena no coinciden o error de datos ingresados."
        flash(mensaje)
       # return redirect(url_for('varios.Singup'))
    return render_template("varios/register.html",frm=frm,titulo="Registro")

@varios.route('/Singup/', methods=['GET','POST'])  # Inicio de Session
def Singup():
    frm= forms.Fr_login(request.form)
    titulo = 'Singup'
    if request.method == 'POST':
        log=Registro.query.filter_by(Nombre=request.form['usuario']).first()
        print(log.retun_contra(frm.contrasena.data))
        if log is not None and log.retun_contra(frm.contrasena.data):
            session['Usuario']=request.form['usuario']

            return(redirect(url_for('varios.main')))
        else:
            return(redirect(url_for('index')))
    return render_template('varios/login.html',titulo=titulo,frm=frm)

@varios.route('/main/')  # Main
def main():
    #valorproductos=productos.query.filter(productos.Codigo).count()
    #valorcliente=Clientes.query.filter(Clientes.id).count()
    return render_template("base_Interna/base.html",valorproductos=1)

@varios.errorhandler(404)  # erro 404 Not found!
def page_not_found(e):
    return render_template("errores.html"), 404
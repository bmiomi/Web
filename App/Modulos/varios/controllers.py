from flask import render_template,flash,request,Blueprint,redirect,url_for
from App import db
from App.Modulos.varios import forms
from App.Modulos.varios.model import Registro

varios=Blueprint('varios',__name__,url_prefix='/varios')

@varios.route('/register/', methods=['GET', 'POST'])  # registro
def register():
    frm=forms.Fr_register(request.form)
    if request.method == 'POST':
        nuevo_user = Registro(frm.Nombre.data,frm.Email.data,frm.contrasena.data)
        db.session.add(nuevo_user)
        db.session.commit()
        return redirect(url_for('varios.Singup'))
    else:
        mensaje = "Constrasena no coinciden"
        flash(mensaje)
    return render_template("varios/register.html",frm=frm,titulo="Registro")


@varios.route('/Singup/', methods=['GET','POST'])  # Inicio de Session
def Singup():
    frm= forms.Fr_login(request.form)
    titulo = 'Singup'
    if request.method =='POST':
        log=Registro.query.filter_by(contrasena=frm.contrasena.data).first()
        print(frm.contrasena.data)
        print(log)
        print()    
        return(redirect(url_for('varios.Singup')))
    return render_template('varios/login.html',titulo=titulo,frm=frm)
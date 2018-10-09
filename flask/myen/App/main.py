#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, redirect,\
    url_for, abort, session, escape, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from config.config import DevelopmentConfig
from Modelos.Modelo import *
from View import Forms


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app


app = create_app()
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)  # erro 404 Not found!
def page_not_found(e):
    return render_template("errores.html"), 404


@app.route("/")  # root!
def index():
    title = "Inicio"
    raiz = " Hola como estas Actualmente te encuentras en la raiz de la paguina "
    return render_template("index.html", titulo=title, raiz=raiz)


@app.route("/main")  # Main
def main():
    valorproductos=productos.query.filter(productos.Codigo).count()
    valorcliente=Clientes.query.filter(Clientes.id).count()
    return render_template("base_Interna/base.html",valorproductos=valorproductos)


@app.route("/register", methods=['GET', 'POST'])  # registro
def register():
    frm = Forms.F_Registro(request.form)
    if request.method == "POST" and frm.validate():
        if frm.contrasena.data == request.form["confpassword"]:
            new_user = F_Registro(
                usuario=frm.Usuario.data,
                contrasena=frm.contrasena.data,
                EMAIL=frm.email.data
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('Singup'))
        else:
            mensaje = "Constrasena no coinciden"
            flash(mensaje)
    return render_template("register.html", frm=frm)


@app.route("/Singup")  # Inicio de Session
def Singup():
    titulo = "Singup"
    return render_template("Singup.html", titulo=titulo)

# --------------------------------Proveedor-----------------------------------

@app.route("/proveedor", methods=['GET', 'POST'])  # registro de proveedor
def proveedor():
    frm = Forms.Fr_Proveedor(request.form)
    if request.method == 'POST':
        pr = db.session.query(Proveedor).filter_by(CI=frm.CI.data).first()
        if frm.validate() and pr is None:
            new_user = Proveedor(razonSolcial=frm.RasonSocial.data,
                                 CI=frm.CI.data,
                                 Nombre=frm.Nombre.data,
                                 Apellido=frm.Apellido.data,
                                 FechaNacimiento=frm.FechaNacimiento.data,
                                 Sexo=frm.Sexo.data)
            db.session.add(new_user)
            db.session.commit()
            flash("Se registrado con exito sus datos")
            redirect(url_for('proveedor'))
        else:
            flash("Error: No se registrado con exito sus Datos")
    return render_template("frproveedor.html", frm=frm)


@app.route('/listaP')  # listado de Proveedores.
def listaP():
    titulo = "Lista Proveedor"
    return render_template("listaP.html", titulo=titulo, listas=Proveedor.query.all())


@app.route('/UpdateP')
def UpdateP():
    updateP = db.session.query(Proveedor).filter_by(
        CI=request.form['CI']).first()
    updateP.Nombre = request.form['Nombre']
    updateP.Apellido = request.form['Apellido']
    updateP.FechaNacimiento = request.form['FechaNacimiento']
    updateP.Sexo = request.form['Sexo']
    db.session.commit()
    return redirect(url_for('lsitaP'))


@app.route('/deleteP/<string:id>')
def deleteP():
    dlTP = db.session.query(Proveedor).filter_by(request.form['CI']).first()
    db.session.commint()
    return redirect(url_for('lsitaP'))


@app.route("/modalP")
def modalP():
    form = Forms.Fr_Proveedor()
    return render_template("modaproveedor.html", frm=form, title="Proveedor")
# --------------------------------CLIENTE-----------------------------------


@app.route("/Cliente", methods=['GET', 'POST'])  # registro de Clientes
def Cliente():
    frm = Forms.Fr_Personal(request.form)
    if request.method == "POST":
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
    return render_template('frcliente.html', frm=frm)


@app.route("/listaC")  # listado de Clientes.
def listaC():
    titulo = "Listado de Clientes"
    res = Clientes.query.all()
    return render_template("listaC.html", titulos=titulo, res=res)


@app.route("/Update", methods=['POST'])
def Update():
    update = db.session.query(Clientes).filter_by(
        id=request.form['id']).first()
    update.Nombre = request.form['Nombre']
    update.Apellido = request.form['Apellido']
    update.FechaNacimiento = request.form['FechaNacimiento']
    db.session.commit()
    return redirect(url_for('listaC'))


@app.route('/delete/<string:id>')
def delete(id):
    dlete = db.session.query(Clientes).filter_by(id=id).delete()
    print(dlete)
    db.session.commit()
    return redirect(url_for('listaC'))


@app.route("/Lp")  # jsonlistacliente
def Lp():
    res = Clientes.query.all()
    listaproveedores = [r.as_dict() for r in res]
    return jsonify({'data': listaproveedores})


@app.route("/modalc")
def modalc():
    form = Forms.Fr_Personal()
    return render_template("modalcliente.html", frm=form, title="Cliente")

# --------------------------------Productos-----------------------------------

@app.route("/Productos", methods=['GET', 'POST'])  # registro de Productos
def Productos():
    frm = Forms.Fr_Productos(request.form)
    if request.method == "POST":
        pr = productos.query.filter_by(Codigo=frm.Codigo.data).first()
        if frm.validate() and pr is None:
            print("dato falda",request.form['Categoria'])
            dbproductos = productos(Codigo=frm.Codigo.data,
                                    nombre=frm.nombre.data,
                                    Precio=frm.Precio.data,
                                    stock=0,
                                    Categoria=request.form['Categoria']

                                    )
            db.session.add(dbproductos)
            db.session.commit() 
            flash("Los datos an sido exitosamente Guardados")
            redirect(url_for('Productos'))
        else:
            flash("Error: No se registrado con exito sus Datos.")
    return render_template('frProductos.html', frm=frm)

@app.route("/listaPr")  # listado de productos.
def listaPr():
	titulo = "Listado de Productos"
	listas = productos.query.order_by(productos.Codigo).all()
	return render_template("listaPr.html", titulo=titulo, listas=listas)

@app.route("/UpdatePr", methods=['POST'])
def UpdatePr():

    update = productos.query().filter_by(
        id=request.form['Codigo']).first()
    update.Nombre = request.form['Nombre']
    update.Apellido = request.form['Categoria']
    update.FechaNacimiento = request.form['Precio']
    update.FechaNacimiento = request.form['stock']
    db.session.commit()
    return redirect(url_for('listaPr'))


@app.route('/deletePr/<string:id>')
def deletePr(id):
    dlete = productos.query.filter_by(codigo=id).delete()
    db.session.commit()
    return redirect(url_for('listaPr'))

@app.route("/modalPr")
def modalPr():
    form = Forms.Fr_Productos()
    return render_template("modalproducto.html", frm=form, title="Producto")

# --------------------------------Categoria-----------------------------------


@app.route("/Categoria",methods=['POST', 'GET']) 
def categoria():
    frm = Forms.Fr_Categoria(request.form)
    if request.method == "POST":
        pr = Categoria.query.filter_by(Nombre=frm.Nombre.data).first()
        if frm.validate and pr is None:
            dbcategoria = Categoria(
                Nombre=frm.Nombre.data
            )
            db.session.add(dbcategoria)
            db.session.commit()
            flash("Los datos an sido exitosamente Guardados")
            redirect(url_for('categoria'))
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
    return render_template("frCategoria.html", frm=frm)


@app.route("/ListaCate")
def ListaCate():
	page=request.args.get('page',1,type=int)
	list=Categoria.query.paginate(page=page,per_page=3)
	return render_template("ListaCate.html", lista=list)
# --------------------------------Almacen-----------------------------------
@app.route('/IngresoAlmacen',methods=['GET','POST'])
def Ingreso():
    frm=Forms.Fr_Almacen()
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
            db.session.commit()
            flash("se  ah registrado con exito sus Datos")
        else:
            flash("Error: No se  ah registrado con exito sus Datos")
    return render_template('almacen.html',frm=frm)

@app.route('/SalidaAlmacen',methods=['GET','POST'])
def SalidaAl():
    frm=Forms.Fr_SalidaAlmacen(request.form)
    return render_template("SalidaAlmacen.html",frm=frm)
@app.route('/MovimientosAlmacen')
def Movimientos():
    return 'Hola baby'
# --------------------------------Modales-----------------------------------

@app.route("/modal")
def modal():
    return render_template("modal.html")


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()  # metodo para crear tablas y la propia db
    app.run( port=8001, debug=True)

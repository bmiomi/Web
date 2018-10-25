from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

csrf = CSRFProtect()
def create_app():
    app = Flask(__name__)
    csrf.init_app(app)
    Bootstrap(app) 
    return app

app = create_app()
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

@app.errorhandler(404)  # erro 404 Not found!
def page_not_found(e):
    return render_template("errores.html"), 404

@app.route('/')  # root!
def index():
    title = "Inicio"
    raiz = " Hola como estas Actualmente te encuentras en la raiz de la paguina "
    return render_template("index.html", titulo=title, raiz=raiz)

@app.route('/main')  # Main
def main():
    #valorproductos=productos.query.filter(productos.Codigo).count()
    #valorcliente=Clientes.query.filter(Clientes.id).count()
    return render_template("base_Interna/base.html",valorproductos=1)



from App.Modulos.cliente.control import cliente
from App.Modulos.Proveedor.controllers import _Proveedor
from App.Modulos.Almacen.controllers import Almacen
from App.Modulos.Categoria.controllers import _Categoria
from App.Modulos.Producto.controllers import Producto
from App.Modulos.varios.controllers import varios

app.register_blueprint(cliente)
app.register_blueprint(_Categoria)
app.register_blueprint(Producto)
app.register_blueprint(_Proveedor)
app.register_blueprint(Almacen)
app.register_blueprint(varios)

with app.app_context():
    db.create_all()  # metodo para crear tablas y la propia db


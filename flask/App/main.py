
from flask import Flask, render_template,request,\
make_response,redirect,url_for,abort,session,escape,flash
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash,check_password_hash
from config import DevelopmentConfig
from Modelo import Registro,db
import Forms

def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	return app

app=create_app()
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

#erro 404 paguina no encontrada
@app.errorhandler(404)
def page_not_found(e):
	return render_template("errores.html"),404

#raiz 
@app.route("/")
def index():
	title="Inicio"
	raiz=" Hola como estas Actualmente te encuentras en la raiz de la paguina "
	return  render_template("index.html",titulo=title,raiz=raiz)


@app.route("/register",methods=['GET','POST'])
def register():
	frm=Forms.F_Registro(request.form)
	if request.method == "POST" and frm.validate():

		if frm.contrasena.data == request.form["confpassword"]:
			
			new_user= Registro(	
							usuario= frm.Usuario.data,
							contrasena=frm.contrasena.data,
							EMAIL=frm.email.data
							  )
			db.session.add(new_user)
			db.session.commit()
			return  redirect(url_for('Singup'))
		else:
			mensaje="Constrasena no coinciden"
			flash(mensaje)
	return render_template("register.html",frm=frm)



@app.route("/Singup",methods=['GET', 'POST'])
def Singup():
	titulo="Singup"
	frm = Forms.F_login(request.form)
	
	if request.method ==  "POST" and frm.validate():

			user=frm.Usuario.data
			mensaje= "Bienvenido {}".format (user)

			flash(mensaje)
			return render_template("index6.html")
#			response=make_response()
#			response.set_cookie('cookiess','cook')

	return render_template("Singup.html", titulo = titulo, frm = frm)

@app.route("/review/<int:numero>")
@app.route("/review")
def review(numero=1):
	pass
	#user= Registro.query.join(Registro).add_colums(login.usuario,Accion.Deportes,Accion.Estudio)
	#return render_template("index6.html",user=user)

@app.route("/Lista") #lista sin conexion a base de datos.
def Lista():
	titulo = "Lista"

	listas=[
		{   
		    'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },

        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },

		 {
            'author': {'nickname': 'Marco'},
          
		    'body': 'The Avengers movie was so wonderfull!'
        },

		 {
            'author': {'nickname': 'carlos'},
            'body': 'The Avengers movie was so ugle!'
        }
	]
	print (listas)
	return render_template("lista.html", titulo=titulo ,listas=listas)

@app.route("/lista/db")#lista con conexion a base de datos.
def listadb():
	return render_template("lista.html",listas=Registro.query.all())

#inicio
@app.route("/Inicio")
def Inicio():
	titulo = "Inicio"
	resivircookie=request.cookies.get('cookiess','default')
	print(resivircookie)
	return render_template("modal.html", titulo=titulo) 


#Registro
#ingreso de datos en la base de datos.

#@app.route("/cookie")
#def cookieread():
#	response=make_response(render_template("index6.html"))
#	response.set_cookie('cookiess','cook')
#	return response

""""
@app.route("/mes",methods=['GET','POST'])
def mes():

	if request.method == "POST":

		_contrasena=generate_password_hash(request.form["contra"],method="sha256")
		new_user= Login(usuario=request.form["usuario"],contrasena=_contrasena)
		Modelo.db.session.add(new_user)
		Modelo.db.session.commit()
		print (new_user,_contrasena)
		return "Registro exito"
	return render_template("sss.html")

"""



"""
#ingreso base de datos
@app.route("/consulta/<texto>")
def consulta(texto):
	new_post=Posts(title=texto)

	Modelo.db.session.add(new_post)
	Modelo.db.session.commit()

	return "fue creado con exito"

@app.route("/consultas/<int:texto>")
def consultas(texto):
	newpost=Posts.query.filter_by(id=texto).first()
	print(newpost.title)
	return "listo"


@app.route("/query")
def query():
	print(Posts.query.all())
	return "listo"





@app.route("/Consult",methods=['GET','POST'])
def consult():

	if request.method == "POST":
		variable=Login.query.filter_by(usuario=request.form["usuario"]).first()
		if variable and check_password_hash(usuario.password,request.form["password"]):
			session["Nombrecokie"]=variable.usuario
			return "Registro exitoso!!!"
		return "Inicio de secion fallido" 
	return render_template("index.html")


# creacion de cookies

@app.route("/cookie/set")
def  cookie():
	respo= make_response(render_template("Index4.html"))
	respo.set_cookie("Nombrecokie","valor")
	return respo
	

# obtener valor de la cookie
@app.route("/cookie/read")
def cookieread():
	username= request.cookies.get("Nombrecokie",None)
	return username
	
@app .route ( '/a' )
def indexs():
    if 'Nombrecokie' in session :
        return 'Logged in as  %s ' % escape ( session [ 'Nombrecokie' ])
    return 'You are not logged in'


@app.route("/upload")
def upload():
	abort(401)
	return redirect(url_for('cookie'))
"""


if __name__ == "__main__":
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()# metodo para crear tablas y la propia db
	app.run( port=8000)


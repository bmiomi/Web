from flask import Flask, render_template,make_response,request

app=Flask(__name__)


@app.route("/cookie/set")
def cookie ():
	respo= make_response(render_template("Index.html"))
	respo.set_cookie("Nombrecokie","valor")
	return respo
	
from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario


# Renderização da página home.html
@app.route("/")
def index():

    return render_template("home.html", titulo = "Agenda de Eventos")


# Renderização da página calendario.html
@app.route("/calendario")
def calendario():

    return render_template("calendario.html", titulo = "Calendário de eventos")


# Renderização da página sobre.html
@app.route("/sobre")
def sobre():

    return render_template("sobre.html", titulo = "Desenvolvedores")


# Renderização da página login.html
@app.route("/login")
def login():

    return render_template("login.html", titulo = "Login")


# Rota para autenticar usuários
@app.route("/autenticar", methods = ["post"])
def autenticar():

    usuario = Usuario.query.filter_by(username = request.form["input_usuario"]).first()

    if usuario:
        if request.form["input_senha"] == usuario.senha:


            return redirect(url_for("index"))
    else:

       return redirect(url_for("login"))
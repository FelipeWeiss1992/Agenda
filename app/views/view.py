from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario


@app.route("/")
def index():

    return render_template("index.html", titulo = "Agenda de Eventos")
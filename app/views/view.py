from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario
import calendar
import datetime


# Renderização da página home.html
@app.route("/")
def index():

    return render_template("home.html", titulo = "Agenda de Eventos")


# Renderização da página sobre.html
@app.route("/sobre")
def sobre():

    return render_template("sobre.html", titulo = "Desenvolvedores")


# Renderização da página login.html
@app.route("/login")
def login():

    proximo = request.args.get("proximo")

    return render_template("login.html", titulo = "Login", proximo = proximo)


# Rota para autenticar usuários.
@app.route("/autenticar", methods = ["post"])
def autenticar():

    lo_usuario = Usuario.query.filter_by(username = request.form["input_usuario"]).first()

    if lo_usuario:
        print(lo_usuario)
        if request.form["input_senha"] == lo_usuario.senha:

            session = lo_usuario.username

            proxima_pagina = request.form["proximo"]

            return redirect(proxima_pagina)
    else:

        return redirect(url_for("login"))


# Rota para logoout.
@app.route("/logout")
def logout():
    pass


# Renderização da página registro.html
@app.route("/registro")
def registro():

    return render_template("registro.html", titulo = "Inscreva-se")


# Rota para cadastrar novo usuário.
@app.route("/cadastrar_usuario", methods = ["post"])
def cadastrar_usuario():

    # Criando variáveis locais.
    lo_nome = request.form["nome"]
    lo_nascimento = request.form["data_nascimento"]
    lo_cpf = request.form["cpf"] # Aplicar filtro para retirar os "." e o "-", estouro de campo no banco de dados.
    lo_nickname = request.form["username"]
    lo_senha = request.form["senha"]

    # Primeiro parametro vindo do Bando de Dados e segundo vindo do Formulário HTML.
    lo_usuario = Usuario.query.filter_by(nome = lo_nome).first()

    if lo_usuario:
        # Usuário já cadastrado.
        if request.form["nome"] == lo_usuario.nome:
            print("Usuário já cadastrado.")

            return redirect(url_for("registro"))
        else:
            lo_novo_usuario = Usuario(nome = lo_nome, data_nascimento = lo_nascimento, cpf = lo_cpf, username = lo_nickname, senha = lo_senha)
            db.session.add(lo_novo_usuario)
            db.session.commit()
            print("Usuário cadastrado com sucesso.")

            return redirect(url_for("login"))
       
    return redirect(url_for("registro"))


# Renderização da página calendario.html
@app.route("/calendario")
def calendario():

    data = datetime.datetime.now()
    cal = calendar.Calendar(firstweekday=6)

    dias_da_semana = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

    calDays = cal.monthdayscalendar(data.year, data.month)

    return render_template("calendario.html", titulo = "Calendário de eventos", calDays = calDays, dias_da_semana = dias_da_semana, ano = data.year, mes = data.month)


# Renderização da página evento.html
@app.route("/evento/<string:dia>/<string:mes>/<string:ano>")
def evento(dia, mes, ano):

    completo = f"{ano}-{mes}-{dia}"

    return render_template("evento.html", titulo = "Cadastro de eventos", completo = completo)


# Rota para cadastrar novo evento.
@app.route("/cadastrar_evento/<dia>")
def cadastrar_evento(dia):
    print(dia)
    pass

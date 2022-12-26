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

    proximo = request.args.get("proximo")

    return render_template("login.html", titulo = "Login", proximo = proximo)


# Rota para autenticar usuários.
@app.route("/autenticar", methods = ["post"])
def autenticar():

    usuario = Usuario.query.filter_by(username = request.form["input_usuario"]).first()

    if usuario:
        print(usuario)
        if request.form["input_senha"] == usuario.senha:

            session = usuario.username

            proxima_pagina = request.form["proximo"]

            return redirect(proxima_pagina)
    else:

        return redirect(url_for("login"))


# Renderização da página registro.html
@app.route("/registro")
def registro():

    return render_template("registro.html", titulo = "Inscreva-se")


# Rota para cadastrar novo usuário.
@app.route("/cadastrar_usuario", methods = ["post"])
def cadastrar_usuario():

    # Criando variáveis locais.
    i_nome = request.form["nome"]
    i_nascimento = request.form["data_nascimento"]
    i_cpf = request.form["cpf"] # Aplicar filtro para retirar os "." e o "-", estouro de campo no banco de dados.
    i_nickname = request.form["username"]
    i_senha = request.form["senha"]

    # Primeiro parametro vindo do Bando de Dados e segundo vindo do Formulário HTML.
    usuario = Usuario.query.filter_by(nome = i_nome).first()


    if usuario:
        # Usuário já cadastrado.
        if request.form["nome"] == usuario.nome:
            print("Usuário já cadastrado.")

            return redirect(url_for("registro"))
        else:
            novo_usuario = Usuario(nome = i_nome, data_nascimento = i_nascimento, cpf = i_cpf, username = i_nickname, senha = i_senha)
            db.session.add(novo_usuario)
            db.session.commit()
            print("Usuário cadastrado com sucesso.")

            return redirect(url_for("login"))
       
    return redirect(url_for("registro"))
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

    lo_proximo = request.args.get("proximo")

    return render_template("login.html", titulo = "Login", proximo = lo_proximo)


# Rota para autenticar usuários.
@app.route("/autenticar", methods = ["post"])
def autenticar():

    lo_usuario = Usuario.query.filter_by(username = request.form["n_usuario"]).first()

    if lo_usuario:

        if request.form["n_senha"] == lo_usuario.senha:

            session["usuario_logado"] = lo_usuario.username

            lo_proxima_pagina = request.form["proximo"]

            return redirect(lo_proxima_pagina)
    else:

        return redirect(url_for("login"))


# Rota para logoout.
@app.route("/logout")
def logout():

    session["usuario_logado"] = None
    print(session)

    return redirect(url_for("index"))


# Renderização da página registro.html
@app.route("/registro")
def registro():

    return render_template("registro.html", titulo = "Inscreva-se")


# Rota para cadastrar novo usuário.
@app.route("/cadastrar_usuario", methods = ["post"])
def cadastrar_usuario():

    # Criando variáveis locais.
    lo_nome = request.form["n_nome"]
    lo_nascimento = request.form["n_data_nascimento"]
    lo_cpf = request.form["n_cpf"] # Aplicar filtro para retirar os "." e o "-", estouro de campo no banco de dados.
    lo_nickname = request.form["n_username"]
    lo_senha = request.form["n_senha"]

    # Primeiro parametro vindo do Bando de Dados e segundo vindo do Formulário HTML.
    lo_usuario = Usuario.query.filter_by(nome = lo_nome).first()

    if lo_usuario:
        # Usuário já cadastrado.

        return redirect(url_for("registro"))
    else:
        lo_novo_usuario = Usuario(nome = lo_nome, data_nascimento = lo_nascimento, cpf = lo_cpf, username = lo_nickname, senha = lo_senha)
        db.session.add(lo_novo_usuario)
        db.session.commit()

        return redirect(url_for("login"))


# Renderização da página calendario.html
@app.route("/calendario")
def calendario():

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("calendario")))
    else:

        data = datetime.datetime.now()
        cal = calendar.Calendar(firstweekday=6)

        dias_da_semana = ("Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb")
        calDays = cal.monthdayscalendar(data.year, data.month)
        mes_ano = f"{str(datetime.datetime.now().strftime('%B'))} - {data.year}"

        return render_template("calendario.html", titulo = "Calendário de eventos", calDays = calDays, dias_da_semana = dias_da_semana, ano = data.year, mes = data.month, mes_ano = mes_ano) 


# Renderização da página evento.html
@app.route("/evento/<string:dia>/<string:mes>/<string:ano>")
def evento(dia, mes, ano):

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("calendario")))
    else:

        lo_completo = f"{ano}-{mes}-{dia}"

        return render_template("evento.html", titulo = "Cadastro de eventos", data_completo = lo_completo)


# Rota para cadastrar novo evento.
@app.route("/cadastrar_evento", methods = ["post"])
def cadastrar_evento():

    lo_usuario = Usuario.query.filter_by(username = session["usuario_logado"]).first()

    # Criando variáveis locais
    lo_data = request.form["n_data"]
    lo_titulo = request.form["n_titulo"]
    lo_descricao = request.form["n_descricao"]
    lo_fk = lo_usuario.id_usuario

    lo_novo_evento = Evento(data_evento = lo_data, titulo = lo_titulo, descricao = lo_descricao, fk_usuario = lo_fk)
    db.session.add(lo_novo_evento)
    db.session.commit()
    # Fazer uma mensagem de Evento cadastrado com sucessso.

    return redirect(url_for("calendario"))


# Renderização da página listar_eventos.html
@app.route("/listar_eventos")
def listar_eventos():

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("calendario")))
    else:
        lo_usuario = Usuario.query.filter_by(username = session["usuario_logado"]).first()
        print("Resultado do SELECT. <=>")
        lo_fk = lo_usuario.id_usuario
        print(lo_usuario.id_usuario)

        lo_eventos = Evento.query.filter_by(fk_usuario = lo_fk).order_by(Evento.data_evento)
        
        return render_template("listar_eventos.html", titulo = "Listar Eventos", eventos = lo_eventos)


@app.route("/editar")
def editar():

    print("Entrou no Editar.")
    pass


@app.route("/deletar")
def deletar():

    print("Entrou no Deletar. ")
    pass

"""@app.route("/editar_eventos/<int:id>")
def editar_eventos(id):

    if "usuario_logado" not in session or session["usuario_logado"] is None:
    
        return redirect(url_for("login", proximo = url_for("editar_eventos")))
    else:
        lo_eventos = Evento.query.filter_by(id = id).first()

    return render_template("editar.html", titulo = "Editar Pessoa", pessoas = pessoa)"""
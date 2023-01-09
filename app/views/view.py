from flask import render_template, request, redirect, flash, url_for,session
from main import db, app
from models.evento import Evento
from models.usuario import Usuario
import calendar
import datetime


                # -------------------------------------- #
                # Home                                   #
                # -------------------------------------- #


# Renderização da página home.html
@app.route("/")
def index():

    if "usuario_logado" not in session or session["usuario_logado"] is None:
        
        return render_template("home.html", titulo = "Agenda de Eventos", login_out = "login", usuario = "", oculto = "oculto")
    else:
        return render_template("home.html", titulo = "Agenda de Eventos", login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


# Renderização da página sobre.html
@app.route("/sobre")
def sobre():

    if "usuario_logado" not in session or session["usuario_logado"] is None:
        
        return render_template("sobre.html", titulo = "Desenvolvedores", login_out = "login", usuario = "", oculto = "oculto")
    else:
        return render_template("sobre.html", titulo = "Desenvolvedores", login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


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

    return redirect(url_for("index"))


                # -------------------------------------- #
                # Usuário                                #
                # -------------------------------------- #


# Renderização da página registro.html
@app.route("/registro")
def registro():

    return render_template("registro.html", titulo = "Inscreva-se", login_out = "login", oculto = "oculto" )


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

        return redirect(url_for("registro"))
    else:
        lo_novo_usuario = Usuario(nome = lo_nome, data_nascimento = lo_nascimento, cpf = lo_cpf, username = lo_nickname, senha = lo_senha)
        db.session.add(lo_novo_usuario)
        db.session.commit()

        return redirect(url_for("login"))


# Renderização da página perfil.html
@app.route("/perfil")
def perfil():

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_perfil = Usuario.query.filter_by(username = session["usuario_logado"]).first()

        return render_template("perfil.html", titulo = "Editar Perfil", perfil = lo_perfil, login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


# Rota para Atualizar perfil do Usuário.
@app.route("/atualizar_perfil", methods = ["POST"])
def atualizar_perfil():

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_perfil = Usuario.query.filter_by(id_usuario = request.form["n_id"]).first()
        lo_perfil.nome = request.form["n_nome"]
        lo_perfil.data_nascimento = request.form["n_data_nascimento"]
        lo_perfil.cpf = request.form["n_cpf"]
        lo_perfil.username = request.form["n_username"]
        lo_perfil.senha = request.form["n_senha"]

        db.session.add(lo_perfil)
        db.session.commit()

        return redirect(url_for("perfil"))


# Rota para Deletar perfil do Usuário.
@app.route("/deletar_perfil/<int:id>")
def deletar_perfil(id):
    
    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_perfil = Usuario.query.filter_by(id_usuario = id).delete()
        db.session.commit()

        session["usuario_logado"] = None

        return redirect(url_for("index"))


                # -------------------------------------- #
                # Eventos                                #
                # -------------------------------------- #


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

        return render_template("calendario.html", titulo = "Calendário de eventos", calDays = calDays, dias_da_semana = dias_da_semana, ano = data.year, mes = data.month, mes_ano = mes_ano, login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


# Renderização da página evento.html
@app.route("/evento/<int:dia>/<int:mes>/<int:ano>")
def evento(dia, mes, ano):

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:

        if dia < 10:
            lo_dia = ("0" + str(dia))
        else:
            lo_dia = str(dia)
        
        if mes < 10:
            lo_mes = ("0" + str(mes))
        else:
            lo_mes = str(mes)

        lo_completo = f"{ano}-{lo_mes}-{lo_dia}"

        return render_template("evento.html", titulo = "Cadastro de eventos", data_completo = lo_completo, login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


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

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_usuario = Usuario.query.filter_by(username = session["usuario_logado"]).first()
        print("Resultado do SELECT. <=>")
        lo_fk = lo_usuario.id_usuario
        print(lo_usuario.id_usuario)

        lo_eventos = Evento.query.filter_by(fk_usuario = lo_fk).order_by(Evento.data_evento)
        
        return render_template("listar_eventos.html", titulo = "Listar Eventos", eventos = lo_eventos, login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


# Renderização da página editar_evento.html
@app.route("/editar_evento/<int:id>")
def editar_evento(id):

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_eventos = Evento.query.filter_by(id_evento = id).first()

        return render_template("editar_evento.html", titulo = "Editar Evento", evento = lo_eventos, login_out = "logout", usuario = session["usuario_logado"], oculto = "visivel")


# Rota para Atualizar Eventos.
@app.route("/atualizar_evento", methods = ["POST"])
def atualizar_evento():

    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_eventos = Evento.query.filter_by(id_evento = request.form["n_id"]).first()
        lo_eventos.data_evento = request.form["n_data"]
        lo_eventos.titulo = request.form["n_titulo"]
        lo_eventos.descricao = request.form["n_descricao"]

        db.session.add(lo_eventos)
        db.session.commit()

        return redirect(url_for("listar_eventos"))


# Rota para Deletar Eventos.
@app.route("/deletar_evento/<int:id>")
def deletar_evento(id):
    
    if "usuario_logado" not in session or session["usuario_logado"] is None:

        return redirect(url_for("login", proximo = url_for("index")))
    else:
        lo_eventos = Evento.query.filter_by(id_evento = id).delete()
        db.session.commit()

        return redirect(url_for("listar_eventos"))
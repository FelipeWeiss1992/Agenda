from main import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String(50), nullable = False) 
    data_nascimento = db.Column(db.Date, nullable = False)
    cpf = db.Column(db.String(11), nullable = False)
    username = db.Column(db.String(50), nullable = False)
    senha = db.Column(db.String(256), nullable = False)


def __repr__(self):
    return '<Name %r>' % self.name

from main import db
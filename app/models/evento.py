from main import db
from models.usuario import Usuario

class Evento(db.Model):
    
    id_evento = db.Column(db.Integer, primary_key = True, autoincrement = True)
    data_evento = db.Column(db.Date, nullable = False)
    titulo = db.Column(db.String(50), nullable = False)
    descricao = db.Column(db.String(200), nullable = False)
    publico = db.Column(db.Boolean, default = False)
    fk_usuario = db.Column(db.Integer, db.ForeignKey(Usuario.id_usuario), nullable = False)


def __repr__(self):
        return '<Name %r>' % self.name
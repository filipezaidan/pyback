from flask.config import Config
from config import bd

class Usuario(bd.Model):
    __tablename__ = 'usuarios'
    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(256))
    email = bd.Column(bd.String(128), unique=True)
    password = bd.Column(bd.String(256))

    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password


    def __repr__(self):
        return '<Usuário com ID = ' + str(self.id) + '>'
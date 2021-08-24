from flask import render_template, request, Blueprint, redirect, url_for
from config import bd
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuarios', __name__, template_folder=TEMPLATES, static_folder=STATIC)


    


# @usuario_blueprint.route('/consultarUsuario')
# def consultarUsuario():
#     usuario_01 = bd.session.query(Usuario).get(1)
#     return 'Usuário com ID = ' + str(usuario_01.id) + '; Nome = ' + usuario_01.nome + '.'


# @usuario_blueprint.route('/consultarUsuarios')
# def consultarUsuarios():
#     usuarios = Usuario.query.all()
#     return render_template('listarUsuarios.html', usuarios=usuarios)
from flask import Flask, render_template
import datetime

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloWorld():
    return 'Sejam bem-vindos!'

@app.route('/home')
def home():
    data = datetime.datetime.now()
    usuarios = ['Filipe Zaidan', 'David Glauber', 'Rodrigo Cézar']
    mostrarUsuarios = True
    return render_template('home.html', dataAtual=data, usuarios=usuarios, mostrarUsuarios=mostrarUsuarios)

#app.run(host='0.0.0.0', port=5000)
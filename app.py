from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from config import bd
from controller.usuario import usuario_blueprint
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)

# Configuração do Banco de Dados
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
bd.init_app(app)

with app.app_context():
    bd.create_all()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    email = request.form.get('email')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first()

    if not user  or not check_password_hash(user.password, password):
        flash('Por favor, verifique suas credenciais e tente novamente!')
        return redirect(url_for('login'))

    return render_template('index.html', user=user)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/changeuserdata')
def userEdit():
    return render_template('userEdit.html')

@app.route('/createAccount', methods=['POST'])
def createAccount():
    nome = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = Usuario.query.filter_by(email=email).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Endereço de e-mail já existe')
        return redirect(url_for('register'))
        #return render_template('register.html', msg='Email em uso')


    usuario = Usuario(nome, email, password=generate_password_hash(password, method='sha256'))
    bd.session.add(usuario)
    bd.session.commit()
    flash('Conta criada com sucesso!')
    return redirect(url_for('login'))


#app.run(host='0.0.0.0', port=5000)
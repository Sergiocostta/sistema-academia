
from flask import Flask, render_template, request, redirect, url_for, session
from treino_predefinido import treinos_prontos
import json

app = Flask(__name__)
app.secret_key = 'segredo'

#@app.route("/")
#def inicio():
#    return render_template("inicio.html")

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['usuario'].strip()  
        senha = request.form['senha']
        tipo = request.form['tipo']

        if len(usuario) == 0:
            return render_template("cadastro.html", erro="Usuário não pode ser vazio ou só espaços.")
        
        if len(senha) < 6:
            return render_template("cadastro.html", erro="A senha deve ter no mínimo 6 caracteres.")
        
        usuarios = carregar_usuarios()

        for u in usuarios:
            if u['usuario'].lower() == usuario.lower():
                return render_template("cadastro.html", erro="Usuário já existe.")

        usuarios.append({'usuario': usuario, 'senha': senha, 'tipo': tipo})

        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f, indent=2)

        return redirect(url_for('login'))

    return render_template("cadastro.html")

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except:
        return []

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuarios = carregar_usuarios()
        usuario = request.form['usuario']
        senha = request.form['senha']
        for u in usuarios:
            if u['usuario'] == usuario and u['senha'] == senha:
                session['usuario'] = usuario
                session['tipo'] = u['tipo']
                return redirect(url_for('painel'))
        return render_template("login.html", erro="Usuário ou senha incorretos")
    return render_template("login.html")

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if session['tipo'] == 'admin':
        return render_template("painel_admin.html", usuario=session['usuario'])
    else:
        return redirect(url_for('mostrar_treinos'))

@app.route('/treinos')
def mostrar_treinos():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('treinos.html', treinos=treinos_prontos)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
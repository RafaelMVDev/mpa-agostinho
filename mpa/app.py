# ==== Bibliotecas ====
from flask import Flask,jsonify, render_template, request, session, redirect, url_for,abort,flash
from json import loads,load

import random
import secrets

# - Blueprints -
from blueprints.homepage.homepage import homepage_bp # Jokenpo blueprint
from blueprints.forca.rotas_forca import fc_bp # Forca blueprint



app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Registrando as Blueprints aqui

app.register_blueprint(fc_bp,url_prefix = "/forca")
app.register_blueprint(homepage_bp,url_prefix = "/")

@app.route("/teste-erros")
def teste_erros():
    return render_template('index.html')

@app.route('/formulario', methods = ["GET","POST"])
def formulario():
    if request.method == "POST":
        # Em uma aplicação real, aqui ocorreria a validação no back-end
        nome = request.form.get('nome')
        email = request.form.get('email')
        print(f"Dados recebidos do formulário: Nome = {nome}, Email = {email}")
        # Simula uma mensagem de sucesso
        
        flash(f"Obrigado por se cadastrar, {nome}!", "sucess")
    return render_template('formulario.html')

@app.route("/area-restrita")
def area_restrita():

    #EM uma aplicação real, aqui voce verificaria se o usuario esta logado
    # COmo não temos um sistema de login, vamos forçar o erro 401 com abort()
    print("Tentativa de acesso à área restrita sem")
    abort(401)

@app.route("/painel-admin")
def painel_admin():
    #Aqui, você verifica se o usuário logado é um administrador.
    # Vamos simular que o usuário não é admin e forçar o erro 403.
    print("Tentativa de acesso ao painel de admin sem permissão")
    abort(403)

# --- Manipuladores de Erro (Error Handler)= ---
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    # A função recebe o objeto de erro como argumento.
    # A retornamos a renderização do nosso template e o código de status 404
    return render_template('404.html'),404

# --- Manipuladores de Erro (Error Handler)= ---
@app.errorhandler(401)
def nao_autorizado(error):
    # A função recebe o objeto de erro como argumento.
    # A retornamos a renderização do nosso template e o código de status 404
    print("OIII")
    return render_template('401.html'),401

# --- Manipuladores de Erro (Error Handler)= ---
@app.errorhandler(403)
def acesso_pro(error):
    # A função recebe o objeto de erro como argumento.
    # A retornamos a renderização do nosso template e o código de status 404
    return render_template('403.html'),403


if __name__ == 'main':
    app.run(debug = True)

for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint}, Methods: {rule.methods}, Rule: {rule.rule}")

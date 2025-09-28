# ==== Bibliotecas ====
from flask import Flask,jsonify, render_template, request, session, redirect, url_for
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


if __name__ == 'main':
    app.run(debug = True)

for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint}, Methods: {rule.methods}, Rule: {rule.rule}")
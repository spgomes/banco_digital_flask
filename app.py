from flask import Flask
from src.routes.contas import contas
from src.routes.clientes import clientes


app = Flask(__name__)
app.register_blueprint(clientes)
app.register_blueprint(contas)

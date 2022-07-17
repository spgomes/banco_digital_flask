from flask import Flask
from src.routes.contas import contas
from src.routes.clientes import clientes


app = Flask(__name__)
app.register_blueprint(clientes)
app.register_blueprint(contas)

@app.route('/')
def pagina_inicial():
    return 'Banco Digital'
    

if __name__ == "__main__":
    app.run()
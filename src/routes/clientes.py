from flask import jsonify, request, Blueprint
from src.entidades.cliente import Cliente
from src.persistencia.bdiServices import MySQLConnection
from src.persistencia.clientePersistence import ClientePersistence
from src.services.clienteServices import ClienteServices

clientes = Blueprint('clientes', __name__)

db = MySQLConnection()
clientePersistence = ClientePersistence(db)
clienteServices = ClienteServices(clientePersistence)

@clientes.route("/cliente", methods=['POST'])
def inserir_cliente():
    dados = request.json

    cliente = Cliente({
        'Nome': dados['Nome'],
        'CPF': dados['CPF'],
        'Telefone': dados['Telefone'],
        'DataNascimento':dados['DataNascimento']
    })
    try:
        if not clienteServices.save_cliente(cliente):
            return "Não foi possivel criar o cliente.", 500 
        if not clienteServices.save_conta(cliente):
            return "Não foi possivel criar a conta.", 500
    except:return "Ok", 204


@clientes.route("/cliente/<cpf>")
def consultar_cliente(cpf):
    try:
        cliente = clienteServices.get_one(cpf)
    except: return "Not Found", 404
    
    resultado = {
        "Nome": cliente.nome,
        "CPF": cliente.cpf,
        "Telefone": cliente.telefone,
        "DataNascimento": cliente.dataNascimento
    }
    return jsonify(resultado)


@clientes.route("/cliente")
def consultar_clientes():
    clientes = clienteServices.consultar()

    return jsonify(clientes)


from flask import jsonify, request, Blueprint
from src.persistencia.bdiServices import MySQLConnection
from src.persistencia.contaPersistence import ContaPersistence
from src.services.contaServices import ContaServices


contas= Blueprint('contas', __name__)

db = MySQLConnection
contaPersistence = ContaPersistence(db)
contaService = ContaServices(contaPersistence)


@contas.route("/conta/<id>")
def consultar_saldo():
    try:
        saldo = contaService.consulta_saldo(id)
    except: "Not Found", 404
    
    return jsonify(saldo/100)


@contas.route("/conta", methods=['POST'])
def deposito():
    conta = request.args.get('conta', None)
    valor = request.args.get('valor', None)

    try:
        contaService.deposito(conta, valor)
    except: "Not Found", 404
    return "Ok", 204


@contas.route("/conta", methods=['POST'])
def retirada():
    conta = request.args.get('conta', None)
    valor = request.args.get('valor', None)

    try:
        contaService.retirada(conta, valor)
    except: "Not Found", 404
    return "Ok", 204


@contas.route("/conta", methods=['POST'])
def transferencia():
    contaOrigem = request.args.get('conta origem', None)
    contaFinal = request.args.get('conta final', None)
    valor = request.args.get('valor', None)

    try:
        contaService.transferencia(contaOrigem, contaFinal, valor)
    except: "Bad Request", 400
    return "Ok", 204


@contas.route("/conta")
def consultar_historico():
     
    id = request.args.get('Numero da conta', None)
    data_menor = request.args.get('Data menor', None)
    data_maior = request.args.get('Data maior', None)
    
    try:
        lista = contaService.consultar_historico(id, data_menor, data_maior)
    except: "Not Found", 404
    
    return jsonify(lista)


@contas.route("/conta")
def consultar_todos_historicos():
    historico = contaService.consultar_todos_historicos()
    return jsonify(historico)

from flask import jsonify, request, Blueprint
from src.persistencia.bdiServices import MySQLConnection
from src.persistencia.contaPersistence import ContaPersistence
from src.services.contaServices import ContaServices


contas= Blueprint("contas", __name__)

db = MySQLConnection()
contaPersistence = ContaPersistence(db)
contaService = ContaServices(contaPersistence)


@contas.route("/conta")
def ola():
    return "Contas"

@contas.route("/conta/saldo/<id>")
def consultar_saldo(id):
    try:
        saldo = contaService.consulta_saldo(id)
    except: "Not Found", 404
    return jsonify(saldo/100)


@contas.route("/conta/deposito/<conta>/<valor>", methods=['POST'])
def deposito(conta, valor):
    try:
        contaService.deposito(conta, valor)
    except: "Not Found", 404
    return "Ok", 204


@contas.route("/conta/retirada/<conta>/<valor>", methods=['POST'])
def retirada(conta, valor):
    try:
        contaService.retirada(conta, valor)
    except: return "Not Found", 404
    return "Ok", 204


@contas.route("/conta/transferencia", methods=['POST'])
def transferencia():
    contaOrigem = request.args.get('conta origem', None)
    contaFinal = request.args.get('conta final', None)
    valor = request.args.get('valor', None)

    try:
        contaService.transferencia(contaOrigem, contaFinal, valor)
    except: "Bad Request", 400
    return "Ok", 204


@contas.route("/conta/<id>/<inicio>/<fim>")
def consultar_historico():

    id = request.args.get('id', None)
    data_menor = request.args.get('inicio', None)
    data_maior = request.args.get('fim', None)
    
    try:
        lista = contaService.consultar_historico(id, data_menor, data_maior)
    except: return "Not Found", 404
    
    return jsonify(lista)


@contas.route("/conta/historico/<id>")
def consultar_todos_historicos():
    historico = contaService.consultar_todos_historicos()
    return jsonify(historico)



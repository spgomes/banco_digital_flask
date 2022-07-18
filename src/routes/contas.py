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

@contas.route("/conta/saldo/<cpf>")
def consultar_saldo(cpf):
    try:
        saldo = contaService.consulta_saldo(cpf)
    except: return "Not Found", 404
    return jsonify(saldo/100)


@contas.route("/conta/deposito", methods=['POST'])
def deposito():
    dados = request.json

    deposito =({
        'contaOrigem': dados['contaOrigem'],
        'Valor': dados['Valor']
    })

    contaOrigem = deposito['contaOrigem']
    valor = deposito['Valor']
    try:
        contaService.deposito(contaOrigem, valor)
    except: return "Not Found", 404
    return "Ok", 204


@contas.route("/conta/retirada", methods=['POST'])
def retirada():
    dados = request.json

    retirada =({
        'contaOrigem': dados['contaOrigem'],
        'Valor': dados['Valor']
    })

    contaOrigem = retirada['contaOrigem']
    valor = retirada['Valor']

    try:
        contaService.retirada(contaOrigem, valor)
    except: return "Not Found", 404
    return "Ok", 204


@contas.route("/conta/transferencia", methods=['POST'])
def transferencia():
    dados = request.json

    transferencia =({
        'contaOrigem': dados['contaOrigem'],
        'contaDestino': dados['contaDestino'],
        'Valor': dados['Valor']
    })

    contaOrigem = transferencia['contaOrigem']
    contaDestino = transferencia['contaDestino']
    valor = transferencia['Valor']
    try:
        contaService.transferencia(contaOrigem, contaDestino, valor)
    except: return "Erro na transferencia", 400
    return "Ok", 204


@contas.route("/conta/<id>/<inicio>/<fim>")
def consultar_historico(id, inicio, fim):
    try:
        lista = contaService.consultar_historico(id, inicio, fim)
    except: return "Not Found", 404
    
    return jsonify(lista)


@contas.route("/conta/historico/<id>")
def consultar_todos_historicos(id):
    historico = contaService.consultar_todos_historicos(id)
    return jsonify(historico)



from datetime import datetime
from src.exceptions.saldo_insuficiente import SaldoInsuficiente
from src.persistencia.contaPersistence import ContaPersistence


class ContaServices:
    def __init__(self, persistence: ContaPersistence) -> None:
        self.persistence = persistence
        self.historico: dict = {}

    def save_deposito(self, historico) -> bool:
        self.persistence.save_deposito(historico)
        return True

    def save_retirada(self, historico) -> bool:
        self.persistence.save_retirada(historico)
        return True


    def save_tranferencia(self, historico) -> bool:
        self.persistence.save_transferencia(historico)
        return True


    def consulta_saldo(self, id) -> int:
        saldo = self.persistence.get_saldo(id)
        return saldo
    

    def consultar_historico(self, id, data_menor, data_maior):
        historico = self.persistence.get_historico(id, data_menor, data_maior)
        return historico
        

    def consultar_todos_historicos(self, id):
        lista = self.persistence.get_all_historico(id)
        return lista


    def deposito(self, contaOrigem, valor):
    
        self.historico = {
            "ValorEntrada": valor,
            "Data": datetime.today().strftime('%Y-%m-%d'),
            "Conta_id": contaOrigem,
        }
        valorEntradaDB = int(valor)
        valorEntradaDB = valorEntradaDB*100
        
        try:
            if self.persistence.deposito_saldo(contaOrigem, valorEntradaDB):
                self.save_deposito(self.historico)
            return True
        except:
            return False


    def retirada(self, contaOrigem, valor):
        valorSaidadb = int(valor)
        valorSaidadb = valorSaidadb *100
        try:
            if self.consulta_saldo(contaOrigem) - valorSaidadb <= 0:
                return False
            if self.persistence.retirada_saldo(contaOrigem, valorSaidadb):
                self.historico = {
                    "ValorSaida": valor,
                    "Data": datetime.today().strftime('%Y-%m-%d'),
                    "Conta_id": contaOrigem,
                }
                self.save_retirada(self.historico)
            return True
        except:
            return False


    def transferencia(self, contaOrigem, contaDestino, valor):
        valorDB = int(valor)
        valorDB = valorDB*100
        try:
            if self.consulta_saldo(contaOrigem) - valorDB <= 0:
                raise SaldoInsuficiente("Saldo insuficiente!")
            if not self.deposito(contaOrigem, valor):
                return False
            self.retirada(contaOrigem, valor)
            self.historico = {
                "ValorSaida": valor,
                "Conta_id": contaOrigem,
                "Data": datetime.today().strftime('%Y-%m-%d'),
                "Conta_destino": contaDestino,
            }
            self.save_tranferencia(self.historico)
            return True
        except:
            return False

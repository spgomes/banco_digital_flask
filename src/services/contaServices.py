from datetime import datetime
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


    def deposito(self, id, valorEntrada):
        self.historico = {
            "ValorEntrada": valorEntrada,
            "Data": datetime,
            "Conta_id": id,
        }
        valorEntrada = valorEntrada*100
        try:
            if self.persistence.deposito_saldo(id, valorEntrada*100):
                self.save_deposito(self.historico)
            return True
        except:
            return False


    def retirada(self, id, valorSaida):
        valorSaida = valorSaida*100
        try:
            if self.consulta_saldo(id) - valorSaida <= 0:
                return False
            if self.persistence.retirada_saldo(id, valorSaida):
                self.historico = {
                    "valorSaida": valorSaida,
                    "Data": datetime,
                    "Conta_id": id,
                }
                self.save_retirada(self.historico)
            return True
        except:
            return False


    def transferencia(self, id, contaDestino, valor):
        contaDestino = contaDestino
        valor = valor*100
        try:
            if self.consulta_saldo(id) - valor <= 0:
                return False
            if not self.deposito(contaDestino, valor):
                return False
            self.retirada(id, valor)
            self.historico = {
                "ValorSaida": valor,
                "Conta_id": id,
                "Data": datetime,
                "Conta_destino": contaDestino,
            }
            self.save_tranferencia(self.historico)
            return True
        except:
            return False




from src.entidades.conta import Conta


class ContaServices():
    def __init__(self) -> None:
        pass


    def save_historico(self) -> bool:
        self.persistence.save()
        return True
    
    def consulta_saldo(self, conta: Conta) -> int:
        saldo = self.persistence.get_saldo(conta.id)
        return saldo
    


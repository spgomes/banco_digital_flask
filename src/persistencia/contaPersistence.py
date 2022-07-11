from src.persistencia.bdiServices import BDIAbstract




class ContaPersistence():
    def __init__(self, conexao: BDIAbstract) -> None:
        self.db = conexao
    

    def get_saldo(self, id):
        saldo = self.db.execute('SELECT Saldo FROM Conta WHERE id = ?', [id])
        return saldo
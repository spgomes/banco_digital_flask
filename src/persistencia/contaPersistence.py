from src.persistencia.bdiServices import BDIAbstract


class ContaPersistence:
    def __init__(self, conexao: BDIAbstract) -> None:
        self.db = conexao

    def get_saldo(self, id):
        saldo = self.db.get_one("SELECT Saldo FROM Conta WHERE id = ?", [id])
        return saldo[0]

    def deposito_saldo(self, id, valorDeposito):
        self.db.execute(
            "UPDATE Conta SET Saldo = Saldo + ? WHERE id = ?", [valorDeposito, id]
        )
        return True

    def retirada_saldo(self, id, valorRetirada):
        self.db.execute(
            "UPDATE Conta SET Saldo = Saldo - ? WHERE id = ?", [valorRetirada, id]
        )
        return True

    def save_deposito(self, historico):
        self.db.execute(
            "INSERT INTO Historico (Data, ValorEntrada, Conta_id) VALUES (?,?,?)",
            [historico["Data"], historico["ValorEntrada"], historico["Conta_id"]],
        )
        return True

    def save_retirada(self, historico):
        self.db.execute(
            "INSERT INTO Historico (Data, ValorSaida, Conta_id) VALUES (?,?,?)",
            [historico["Data"], historico["ValorSaida"], historico["Conta_id"]],
        )
        return True

    def save_transferencia(self, historico):
        self.db.execute(
            "INSERT INTO Historico (Data, ValorSaida, Conta_id, Conta_destino) VALUES (?,?,?,?)",
            [
                historico["Data"],
                historico["ValorSaida"],
                historico["Conta_id"],
                historico["Conta_destino"],
            ],
        )
        return True


    def get_all_historico(self, id):
        lista = self.db.get_all("SELECT* FROM Historico WHERE Conta_id = ?", [id])
        return lista

    def get_historico(self, id, data_menor, data_maior):
        lista = (
            "SELECT * FROM Operacao WHERE conta_id = ? and datediff(DT_Simulacao, ?) >= 0 and datediff(?, DT_Simulacao) >= 0",
            [id, data_menor, data_maior],
        )
        return lista


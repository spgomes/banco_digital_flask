from src.persistencia.bdiServices import BDIAbstract


class ContaPersistence:
    def __init__(self, conexao: BDIAbstract) -> None:
        self.db = conexao
    """
    A persistência executa os comando SQL.
    """


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
        lista = self.db.get_all("SELECT Data, ValorSaida, ValorEntrada FROM Historico WHERE Conta_id = ?", [id])
        retorno = []
        for registro in lista:
            retorno.append({
                "Data": registro[0].strftime('%Y-%m-%d'),
                "ValorSaida": registro[1],
                "ValorEntrada": registro[2]
            })
        return retorno


    def get_historico(self, id, inicio, fim):
        print(inicio, fim)
        lista = self.db.get_all(
            """SELECT Data, ValorSaida, ValorEntrada 
            FROM Historico 
            WHERE Conta_id = ? and datediff(Data, ?) >= 0 and datediff(?, Data) >= 0 order by Data""",
            [id, inicio, fim],
        )

        retorno = []
        for registro in lista:
            retorno.append({
                "Data": registro[0].strftime('%Y-%m-%d'),
                "ValorSaida": registro[1],
                "ValorEntrada": registro[2]
            })
        return retorno


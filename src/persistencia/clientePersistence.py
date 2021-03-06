from src.entidades.cliente import Cliente
from src.persistencia.bdiServices import BDIAbstract


class ClientePersistence:
    """
    A persistĂȘncia executa os comando SQL.
    """
    def __init__(self, conexao: BDIAbstract) -> None:
        self.db = conexao


    def save_cliente(self, dados_cliente: dict) -> bool:
        try:
            self.db.execute(
                """INSERT INTO Cliente (Nome, CPF, Telefone, DataNascimento) 
                    VALUES (?, ?, ?, ?)""",
                [
                    dados_cliente["Nome"],
                    dados_cliente["CPF"],
                    dados_cliente["Telefone"],
                    dados_cliente["DataNascimento"],
                ],
            )
            return True
        except:
            return False


    def save_conta(self, cliente: Cliente) -> bool:
        dados_conta = {
            "Cliente_CPF": cliente.cpf,
            "Saldo": 0,
        }
        try:
            self.db.execute(
                """INSERT INTO Conta (Cliente_CPF, Saldo) 
                    VALUES (?, ?)""",
                [
                    dados_conta["Cliente_CPF"],
                    dados_conta["Saldo"],
                ],
            )
            return True
        except:
            return False


    def get_one(self, cpf) -> dict:
        retorno = self.db.get_one(
            """SELECT CPF, Nome, Telefone, DataNascimento, Conta.id 
                FROM Cliente LEFT JOIN Conta ON (CPF=Cliente_CPF)
                WHERE CPF = ?""",[cpf]
        )
        return {
            "CPF": retorno[0],
            "Nome": retorno[1],
            "Telefone": retorno[2],
            "DataNascimento": retorno[3],
            "id": retorno[4],
        }


    def get_all(self) -> list:
        return self.db.get_all("SELECT * FROM Cliente", [])

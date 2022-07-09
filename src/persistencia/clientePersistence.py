
from src.entidades.cliente import Cliente
from src.persistencia.bdiServices import MySQLConnection




class ClientePersistence():
    def __init__(self, conexao: MySQLConnection) -> None:
        self.db = conexao
        



    def save_cliente(self, dados_cliente: dict) -> bool:
        try:
            self.db.execute(
                """INSERT INTO Cliente (Nome, CPF, Telefone, DataNascimento) 
                    Values (%(Nome)s, %(CPF)s, %(Telefone)s, %(DataNascimento)s)""",
                    {
                        'Nome': dados_cliente['Nome'],
                        'CPF': dados_cliente['CPF'],
                        'Telefone': dados_cliente['Telefone'],
                        'DataNascimento': dados_cliente['DataNascimento']
                    }
            )
            return True
        except:
            return False


    def save_conta(self, dados_conta:dict) -> bool:
        try:
            self.db.execute(
                """INSERT INTO Conta (Cliente_id, Saldo, id) 
                    Values (%(Cliente_id)s, %(Saldo)s, %(id)s )""",
                    {
                        'id': dados_conta['id'],
                        'Cliente_id': dados_conta['Cliente_id'],
                        'Saldo': dados_conta['Saldo']
                    }
            )
            return True
        except:
            return False


    def get_one(self, cliente: Cliente) -> dict:
        return self.db.get_one("""SELECT Cliente.*, Conta.id FROM Cliente JOIN Conta USING(Cliente_id)
                                WHERE CPF = %(CPF)s""", {'CPF': cliente.cpf})

    def get_all(self) -> list:
        return self.db.get_all('SELECT * FROM Cliente',{})


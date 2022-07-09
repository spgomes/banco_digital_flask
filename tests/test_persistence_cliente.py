import sqlite3
from unittest import TestCase
from src.entidades.cliente import Cliente
from src.persistencia.bdiServices import SQLiteConnection
from src.persistencia.clientePersistence import ClientePersistence

conn = sqlite3.connect(':memory:')

print("Connection is established: Database is created in memory")


class TestPersistenceCliente(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cliente = None
        self.dados_cliente = None
        self.clientePersistence = None

    def setUp(self) -> None:
        self.dados_cliente = {
            'id' : '12345678-1234-5678-1234-567812345678',
            'Nome': 'José',
            'CPF': '83153824894',
            'Telefone': '35911112222', 
            'DataNascimento':'22/33/2040' 
            }
        self.cliente = Cliente(self.dados_cliente)
        self.clientePersistence = ClientePersistence(SQLiteConnection(conn))
        
        try:
            cur = conn.cursor()
            cur.execute("""
                        CREATE TABLE Cliente
                        (Nome VARCHAR(100) NOT NULL PRIMARY KEY,
                        CPF VARCHAR(11) NOT NULL,
                        Telefone VARCHAR(11) NOT NULL,
                        DataNascimento VARCHAR(10) NOT NULL)""")
            conn.commit()

            cur.execute("""
                        CREATE TABLE Conta
                        (id INT NOT NULL PRIMARY KEY,
                        Saldo INT NOT NULL,
                        Cliente_CPF VARCHAR(11) NOT NULL)""")
            conn.commit()
            
            cur.execute("""
                        CREATE TABLE Historico(
                        id INT NOT NULL PRIMARY KEY,
                        Data DATE NOT NULL,
                        ValorSaida INT NULL,
                        ValorEntrada INT NULL,
                        Conta_id INT NOT NULL)""")
            conn.commit()
        except Exception as e: print (e)


    def tearDown(self) -> None:
        cur = conn.cursor()
        cur.execute("DROP TABLE Historico")
        cur.execute("DROP TABLE Conta")
        cur.execute("DROP TABLE Cliente")
        conn.close()


    def test_deve_retornar_cliente(self):
        return self.assertEqual(self.clientePersistence.get_one(self.cliente), self.cliente.__dados_cliente)
import sqlite3
from unittest import TestCase
from src.entidades.cliente import Cliente
from src.entidades.conta import Conta
from src.persistencia.bdiServices import SQLiteConnection
from src.persistencia.clientePersistence import ClientePersistence
from src.persistencia.contaPersistence import ContaPersistence

conn = sqlite3.connect(':memory:')

print("Connection is established: Database is created in memory")


class TestPersistenceCliente(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cliente = None
        self.dados_cliente = None
        self.clientePersistence = None
        self.conta = None
        self.contaPersistence = None

    def setUp(self) -> None:
        self.dados_cliente = {
            'Nome': 'José',
            'CPF': '83153824894',
            'Telefone': '35911112222', 
            'DataNascimento':'2012-12-01' 
            }
        self.cliente = Cliente(self.dados_cliente)
        self.conta = Conta
        self.contaPersistence = ContaPersistence(SQLiteConnection(conn))
        self.clientePersistence = ClientePersistence(SQLiteConnection(conn))
        
        try:
            cur = conn.cursor()
            cur.execute("""
                        CREATE TABLE Cliente
                        (Nome VARCHAR(100) NOT NULL PRIMARY KEY,
                        CPF VARCHAR(11) NOT NULL,
                        Telefone VARCHAR(11) NOT NULL,
                        DataNascimento DATE NOT NULL)""")
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

            cur.execute('INSERT INTO Conta(id, Saldo, Cliente_CPF) Values (1, 100000, 83153824894)')
        
        except Exception as e: print (e)


    def tearDown(self) -> None:
        cur = conn.cursor()
        cur.execute("DROP TABLE Historico")
        cur.execute("DROP TABLE Conta")
        cur.execute("DROP TABLE Cliente")
        conn.close()


    def test_deve_retornar_cliente(self):
        self.assertTrue(self.clientePersistence.save_cliente(self.cliente.to_db()))
        retorno = self.clientePersistence.get_one(self.cliente)
        self.assertEqual(retorno['CPF'], self.cliente.cpf)
        self.assertEqual(retorno['Nome'], self.cliente.nome)
        self.assertEqual(retorno['Telefone'], self.cliente.telefone)
        
    
    def test_retorno_saldo_conta(self):
        self.assertEqual(self.contaPersistence.get_saldo(1), 100000)
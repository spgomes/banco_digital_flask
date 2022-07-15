import datetime
import sqlite3
from unittest import TestCase
from src.entidades.cliente import Cliente
from src.entidades.conta import Conta
from src.persistencia.bdiServices import SQLiteConnection
from src.persistencia.clientePersistence import ClientePersistence
from src.persistencia.contaPersistence import ContaPersistence

conn = sqlite3.connect(':memory:')

print("Connection is established: Database is created in memory")


class TestPersistence(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.conta = None
        self.cliente = None
        self.historico = None
        self.dados_cliente = None
        self.contaPersistence = None
        self.clientePersistence = None

    def setUp(self) -> None:
        self.historico = {'Data':'2022/07/12', 'ValorSaida':700, 'ValorEntrada':900, 'Conta_id': 1, 'Conta_destino': 2}
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
                        id INT PRIMARY KEY,
                        Data DATE NOT NULL,
                        ValorSaida INT NULL,
                        ValorEntrada INT NULL,
                        Conta_id INT NULL,
                        Conta_destino INT NULL
                        )""")
            conn.commit()

            cur.execute('INSERT INTO Conta(id, Saldo, Cliente_CPF) Values (1, 100000, 83153824894)')
            
        
        except Exception as e: print (e)


    def tearDown(self) -> None:
        cur = conn.cursor()
        cur.execute("DROP TABLE Historico")
        cur.execute("DROP TABLE Conta")
        cur.execute("DROP TABLE Cliente")



    def test_deve_retornar_cliente(self):
        self.assertTrue(self.clientePersistence.save_cliente(self.cliente.to_db()))
        cpf = self.cliente.cpf
        retorno = self.clientePersistence.get_one(cpf)
        self.assertEqual(retorno['CPF'], self.cliente.cpf)
        self.assertEqual(retorno['Nome'], self.cliente.nome)
        self.assertEqual(retorno['Telefone'], self.cliente.telefone)
        
    
    def test_retorno_saldo_conta(self):
        self.assertEqual(self.contaPersistence.get_saldo(1), 100000)
    
    def test_update_saldo(self):
        self.assertTrue(self.contaPersistence.deposito_saldo(1, 100000))
        self.assertEqual(self.contaPersistence.get_saldo(1), 200000)
        self.assertTrue(self.contaPersistence.retirada_saldo(1, 100000))
        self.assertEqual(self.contaPersistence.get_saldo(1), 100000)
        

    def test_save_historico(self):
        self.assertTrue(self.contaPersistence.save_deposito(self.historico))
        self.assertTrue(self.contaPersistence.save_transferencia(self.historico))
        self.assertTrue(self.contaPersistence.save_retirada(self.historico))

    def test_retorno_historico(self):
        self.assertTrue(self.contaPersistence.save_deposito(self.historico))
        retorno_historico = self.contaPersistence.get_all_historico(1)
        self.assertEqual(retorno_historico[0][3], self.historico['ValorEntrada'])
        retorno_historico1 = self.contaPersistence.get_historico(1, '2022/07/12', '2022/07/13')
        self.assertTrue(retorno_historico1[0], self.historico)
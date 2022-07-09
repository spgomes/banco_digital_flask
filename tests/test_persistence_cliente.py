import sqlite3
from unittest import TestCase
from sqlite3 import Error as Err
from src.entidades.cliente import Cliente
from src.persistencia.clientePersistence import ClientePersistence



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
        self.clientePersistence = ClientePersistence
        
        try:
            conn = sqlite3.connect(':memory:')
            cur = conn.cursor()
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS `banco_flask`.`Cliente` 
                    (
                    `Nome` VARCHAR(100) NOT NULL,
                    `CPF` VARCHAR(11) NOT NULL,
                    `Telefone` VARCHAR(11) NOT NULL,
                    `DataNascimento` VARCHAR(10) NOT NULL,
                    PRIMARY KEY (`CPF`)
                    )
                """)
            conn.commit()

            cur.execute("""
                    CREATE TABLE IF NOT EXISTS `banco_flask`.`Conta` 
                    (
                    `id` INT AUTO_INCREMENT=100000 NOT NULL,
                    `Saldo` INT NOT NULL,
                    `Cliente_CPF` VARCHAR(11) NOT NULL,
                    PRIMARY KEY (`id`),
                    INDEX `fk_Conta_Cliente1_idx` (`Cliente_CPF` ASC) VISIBLE,
                    CONSTRAINT `fk_Conta_Cliente1`
                        FOREIGN KEY (`Cliente_CPF`)
                        REFERENCES `banco_flask`.`Cliente` (`CPF`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        )
        """)
            conn.commit()
            
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS `banco_flask`.`Historico` 
                    (
                    `id` INT NOT NULL,
                    `Data` DATE NOT NULL,
                    `ValorSaida` INT NULL,
                    `ValorEntrada` INT NULL,
                    `Conta_id` INT NOT NULL,
                    PRIMARY KEY (`Conta_id`),
                    INDEX `fk_Historico_Conta1_idx` (`Conta_id` ASC) VISIBLE,
                    CONSTRAINT `fk_Historico_Conta1`
                        FOREIGN KEY (`Conta_id`)
                        REFERENCES `banco_flask`.`Conta` (`id`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION
                        )
        """)
            conn.commit()
        except Err: print(Err)


    def tearDown(self) -> None:
        conn = sqlite3.connect(':memory:')
        cur = conn.cursor()

        cur.execute("DROP TABLE Historico")
        cur.execute("DROP TABLE Conta")
        cur.execute("DROP TABLE Cliente")
        conn.close()


    def test_deve_retornar_cliente(self):
        return self.assertEqual(self.clientePersistence.get_one(self.cliente), self.cliente.__dados_cliente)
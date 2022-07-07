
from unittest import TestCase

from src.entidades.conta import Conta



class TestConta(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.conta = None
        self.dados_conta = None
    

    def setUp(self) -> None:
        self.dados_conta = {'idConta':'223344', 'Saldo':'1000', 'Historico': '[]', 'idCliente':'ID'}
        self.conta = Conta(self.dados_conta)
    

    def test_deve_retornar_id(self):
        self.assertEqual(self.conta.idConta, self.dados_conta['idConta'])
    
    def test_deve_retornar_saldo(self):
        self.assertEqual(self.conta.saldo, self.dados_conta['Saldo'])
    

    def test_deve_retornar_id_cliente(self):
        self.assertEqual(self.conta.idCliente, self.dados_conta['idCliente'])
    
    
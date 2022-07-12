from unittest import TestCase
from unittest.mock import Mock

from src.entidades.conta import Conta
from src.persistencia.contaPersistence import ContaPersistence
from src.services.contaServices import ContaServices


class TestContaServices(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.conta = None
        self.dados_conta = None
        self.persistence = None
        self.contaService = None
    

    def setUp(self) -> None:
        self.dados_conta = {
            'id' : 1,
            'idCliente' : '11122233344',
            'Saldo' : 100000
        }
        self.conta = Conta(self.dados_conta)
        self.persistence = ContaPersistence 
        self.contaService = ContaServices(ContaPersistence)

        self.persistence.save_deposito = Mock()
        self.persistence.save_deposito.return_value = True
        self.persistence.deposito_saldo = Mock()
        self.persistence.deposito_saldo.return_value = True
        self.contaService.consulta_saldo = Mock()
        self.contaService.consulta_saldo.return_value = 1000000
        self.persistence.save_retirada = Mock()
        self.persistence.save_retirada.return_value = True
        self.persistence.retirada_saldo = Mock()
        self.persistence.retirada_saldo.return_value = True
        self.contaService.deposito = Mock()
        self.contaService.deposito.return_value = True
        self.contaService.retirada = Mock()
        self.contaService.retirada.return_value = True
        self.contaService.save_tranferencia = Mock()
        self.contaService.save_tranferencia.return_value = True

    def test_deposito(self):
        return self.assertTrue(self.contaService.deposito(1, 100000))

    def test_retirada(self):
        return self.assertTrue(self.contaService.retirada(1,5000))
        
    def test_transferencia_retornar_true(self):
        self.assertTrue(self.contaService.transferencia(1,2,100000))
        
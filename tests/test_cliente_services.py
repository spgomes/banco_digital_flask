from unittest import TestCase
from unittest.mock import Mock
from src.entidades.cliente import Cliente
from src.persistencia.clientePersistence import ClientePersistence
from src.services.clienteServices import ClienteServices


class TesteClienteServices(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cliente = None
        self.dados_cliente = None
        self.clienteServices = None
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
        self.clienteServices = ClienteServices(ClientePersistence)
        self.clientePersistence = ClientePersistence


    def test_cadastrar_cliente(self):
        self.clientePersistence.save_cliente = Mock()
        self.clientePersistence.save_cliente.return_value = True
        return self.assertTrue(self.clienteServices.save_cliente(self.cliente))
    
    def test_criar_conta(self):
        self.clientePersistence.save_conta = Mock()
        self.clientePersistence.save_conta.return_value = True
        self.clientePersistence.get_one = Mock()
        self.clientePersistence.get_one.return_value = self.cliente
        return self.assertTrue(self.clienteServices.save_conta(self.cliente))

    def test_consultar_contas(self):
        self.clientePersistence.get_all = Mock()
        self.clientePersistence.get_all.return_value = ['212121', '343456']
        return self.assertEqual(self.clienteServices.consultar(), ['212121', '343456'])

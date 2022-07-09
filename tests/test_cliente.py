from unittest import TestCase
from validate_docbr import CPF
from src.entidades.cliente import Cliente

cpf = CPF()


class TestCliente(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.cliente = None
        self.dados_cliente = None
        


    
    def setUp(self) -> None:
        self.dados_cliente = {'id' : '1234ddga','Nome': 'José', 'CPF': '11122233345','Telefone': '35911112222', 'DataNascimento':'22/33/2040' }
        self.cliente = Cliente(self.dados_cliente)

    def test_deve_retornar_nome(self):
        self.assertEqual(self.cliente.nome, self.dados_cliente['Nome'])
    
    def test_deve_retornar_CPF(self):
        self.assertEqual(self.cliente.cpf, self.dados_cliente['CPF'])
    
    def test_deve_retornar_telefone(self):
        self.assertEqual(self.cliente.telefone, self.dados_cliente['Telefone'])
    

    def test_nao_deve_alterar_nome(self):
        with self.assertRaises(AttributeError):
            self.cliente.nome = "Pedro"
    
    def test_nao_deve_alterar_cpf(self):
        with self.assertRaises(AttributeError):
            self.cliente.cpf = "22233344455"

    def test_nao_deve_alterar_telefone(self):
        with self.assertRaises(AttributeError):
            self.cliente.telefone = "35922334455"
            
    def test_cpf_is_not_Valid(self):
        return self.assertFalse(cpf.validate(self.cliente.cpf))

    def test_nome_isValid(self):
        return self.assertTrue(self.cliente.nome_isValid) 

    def test_telefone_isValid(self):
        return self.assertTrue(self.cliente.telefone_isValid)

    def test_data_nascimento_isValid(self):
        return self.assertTrue(self.cliente.dataNascimento_isValid)  
        
from validate_docbr import CPF

from src.exceptions.validate_error import ValidateError

cpf = CPF()

class Cliente():
    def __init__(self, dados_cliente: dict) -> None:
        self.__dados_cliente = dados_cliente

    
    @property
    def id(self):
        return self.__dados_cliente['ID']
    
    
    @property
    def nome(self):
        return self.__dados_cliente['Nome']

    
    @property
    def cpf(self):
        return self.__dados_cliente['CPF']

    
    @property
    def telefone(self):
        return self.__dados_cliente['Telefone']

    
    @property
    def dataNascimento(self):
        return self.__dados_cliente['DataNascimento']


    def to_db(self):
        return self.__dados_cliente

    def nome_isValid(self) -> bool:
        return self.nome != None
    
    def telefone_isValid(self) -> bool:
        return len(str(self.telefone)) == 11
    
    def dataNascimento_isValid(self) -> bool:
        return len(str(self.dataNascimento)) == 10

    def cpf_isValid(self) -> bool:
        return cpf.validate(self.cpf)
    
    def isValid(self):
        if not self.nome_isValid(self.nome):
            raise ValidateError("O campo 'nome' deve ser preenchido!")
        if not self.cpf_isValid(self.cpf):
            raise ValidateError("CPF inválido!")
        if not self.dataNascimento_isValid(self.dataNascimento):
            raise ValidateError("Data de nascimento em formato inválido!")
        if not self.telefone_isValid(self.telefone):
            raise ValidateError("Telefone em formato inválido!")
        return True

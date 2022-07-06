from validate_docbr import CPF

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
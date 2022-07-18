from src.exceptions.validade_error import ValidateError


class Conta:
    def __init__(self, dados_conta: dict) -> None:
        self.__dados_conta = dados_conta

    @property
    def id(self):
        return self.__dados_conta["id"]

    @property
    def saldo(self):
        return self.__dados_conta["Saldo"]

    @property
    def idCliente(self):
        return self.__dados_conta["idCliente"]

    def to_db(self):
        return self.__dados_conta

        """
        Funções de validação para a entidade. Os dados devem estar dentro do padrão para serem validos.
        """
    
    def saldo_isValid(self):
        return self.saldo >= 0

    def idCliente_isValid(self):
        return len(self.idCliente) == 11

    def isValid(self):
        """
        É chamada pelo service para fazer as validações da entidade.
        
        """
        if not self.idCliente_isValid(self.idCliente):
            raise ValidateError("ID do cliente inválido!")
        if not self.saldo_isValid(self.saldo):
            raise ValidateError("Saldo não pode ser menor que 0!")
        if not self.idConta_isValid(self.id):
            raise ValidateError("ID da conta inválido!")
        return True

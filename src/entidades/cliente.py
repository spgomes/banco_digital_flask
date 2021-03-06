from validate_docbr import CPF
from src.exceptions.validade_error import ValidateError

cpf = CPF()


class Cliente:
    def __init__(self, dados_cliente: dict) -> None:
        self.__dados_cliente = dados_cliente

    @property
    def nome(self):
        return self.__dados_cliente["Nome"]

    @property
    def cpf(self):
        return self.__dados_cliente["CPF"]

    @property
    def telefone(self):
        return self.__dados_cliente["Telefone"]

    @property
    def dataNascimento(self):
        return self.__dados_cliente["DataNascimento"]

    def to_db(self):
        return self.__dados_cliente


    """
        Funções de validação para a entidade. Os dados devem estar dentro do padrão para serem validos.
        Nome: str
        Telefone: str de exatos 11 dígitos
        Data de Nascimento: str de exatos 10 dígitos
        CPF: Válido conforme o validador 'validate_docbr'

    """
    def nome_isValid(self) -> bool:
        return self.nome != None

    def telefone_isValid(self) -> bool:
        return len(str(self.telefone)) == 11

    def dataNascimento_isValid(self) -> bool:
        return len(str(self.dataNascimento)) == 10

    def cpf_isValid(self) -> bool:
        return cpf.validate(self.cpf)

    def isValid(self):
        """
        É chamada pelo service para fazer as validações da entidade.

        """
        if not self.nome_isValid():
            raise ValidateError("O campo 'nome' deve ser preenchido!")
        if not self.cpf_isValid():
            raise ValidateError("CPF inválido!")
        if not self.dataNascimento_isValid():
            raise ValidateError("Data de nascimento em formato inválido!")
        if not self.telefone_isValid():
            raise ValidateError("Telefone em formato inválido!")
        return True

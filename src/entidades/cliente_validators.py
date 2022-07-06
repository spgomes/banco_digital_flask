

from exceptions.validate_error import ValidateError
from src.entidades.cliente import Cliente


class ClienteValidators():
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente

    def isValid(self):
        if not self.cliente.nome_isValid(self.cliente.nome):
            raise ValidateError("O campo 'nome' deve ser preenchido!")
        if not self.cliente.cpf_isValid(self.cliente.cpf):
            raise ValidateError("CPF inválido!")
        if not self.cliente.dataNascimento_isValid(self.cliente.dataNascimento):
            raise ValidateError("Data de nascimento em formato inválido!")
        if not self.cliente.telefone_isValid(self.cliente.telefone):
            raise ValidateError("Telefone em formato inválido!")
        return True

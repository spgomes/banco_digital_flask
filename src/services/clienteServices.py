from src.entidades.cliente import Cliente
from src.exceptions.client_not_found import ClientNotFound
from src.exceptions.criar_cliente import ClienteNaoCriado
from src.persistencia.clientePersistence import ClientePersistence


class ClienteServices:
    def __init__(self, persistence: ClientePersistence) -> None:
        self.persistence = persistence

    def save_cliente(self, cliente: Cliente) -> bool:
        if cliente.isValid():
            self.persistence.save_cliente(cliente.to_db())
            return True
        raise ClienteNaoCriado("Não foi possível criar o cliente.")

    def save_conta(self, cliente: Cliente) -> bool:
        try:
            if self.get_one(cliente.cpf) is None:
                raise ClientNotFound("Esse cliente não existe!")
            self.persistence.save_conta(cliente)
            return True
        except:
            return False

    def consultar(self) -> list:
        return self.persistence.get_all()

    def get_one(self, cpf: int) -> Cliente:
        dados_cliente = self.persistence.get_one(cpf)
        cliente = Cliente(dados_cliente)
        return cliente

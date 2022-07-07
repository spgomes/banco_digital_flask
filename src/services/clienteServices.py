

from src.entidades.cliente import Cliente
from src.exceptions.client_not_found import ClientNotFound



class ClienteServices():
    def __init__(self) -> None:
        pass

    def save_cliente(self, cliente: Cliente) -> bool:
        if cliente.isValid():
            self.persistence.save_cliente(cliente.to_db())
            return True
        return False

    def save_conta(self, cliente: Cliente) -> bool:
        try:
            if self.get_cliente(self, cliente.__dados_cliente['id']) is None:
                raise ClientNotFound("Esse cliente não existe!")
            self.persistence.save_conta(cliente.__dados_cliente['id'])
            return True
        except:
            return False
    
    def consultar(self, cliente: Cliente) -> list:
        return self.persistence.get_all()
    
    def get_one(self, id: int) -> Cliente:
        dados_cliente = self.persistence.get_one(id)
        cliente = Cliente(dados_cliente)
        return cliente


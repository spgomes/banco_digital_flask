from src.exceptions.base_error import BaseError


class SaldoInsuficiente(BaseError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

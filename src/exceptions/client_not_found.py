
from src.exceptions.base_error import BaseError


class ClientNotFound(BaseError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
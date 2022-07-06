
from exceptions.base_error import BaseError


class ValidateError(BaseError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

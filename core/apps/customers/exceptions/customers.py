from dataclasses import dataclass

from core.apps.customers.exceptions.base import CodeException


@dataclass(eq=False)
class InvalidCustomerTokenException(CodeException):
    token: str

    @property
    def message(self):
        return "Customer was not found for the given token."

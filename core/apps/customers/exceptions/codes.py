from dataclasses import dataclass

from core.apps.customers.exceptions.base import CodeException


@dataclass(eq=False)
class CodeWasNotFoundException(CodeException):
    code: str

    @property
    def message(self):
        return f"{self.code=} not was found"


@dataclass(eq=False)
class CodesAreNotEqualException(CodeException):
    code: str
    cached_code: str
    customer_phone: str

    @property
    def message(self):
        return f"{self.code=} is not equal to {self.cached_code=}"

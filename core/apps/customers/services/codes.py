from abc import ABC, abstractmethod

from core.apps.customers.entities.customers import CustomerEntity


class ICodeSerivce(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str: ...

    def validate(self, code: str, customer: CustomerEntity) -> None: ...

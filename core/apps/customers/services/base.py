from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.apps.customers.entities.customers import CustomerEntity


@dataclass(eq=False)
class IAuthService(ABC):
    customer_service: "ICustomerService"
    code_service: "ICodeSerivce"
    sender_service: "ISenderService"

    @abstractmethod
    def authorize(self, phone: str): ...

    @abstractmethod
    def confirm(self, token: str): ...


class ICodeSerivce(ABC):
    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str: ...

    def validate(self, code: str, customer: CustomerEntity) -> None: ...


class ISenderService(ABC):
    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None: ...


class ICustomerService(ABC):
    @abstractmethod
    def get_or_create_customer_by_phone(self, phone: str) -> CustomerEntity: ...

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str: ...

    @abstractmethod
    def get(self, phone: str) -> CustomerEntity: ...

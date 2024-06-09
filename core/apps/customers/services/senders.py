from dataclasses import dataclass
from typing import Iterable
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.services.base import ISenderService


@dataclass
class DummySenderService(ISenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code {code} was sent to user: {customer}")


@dataclass
class EmailSenderService(ISenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code {code} was sent to user: {customer} via email")


@dataclass
class PushSenderService(ISenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code {code} was sent to user: {customer} via fcm")


@dataclass
class ComposedSenderService(ISenderService):
    sender_services: Iterable[ISenderService]

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        for service in self.sender_services:
            service.send_code(customer=customer, code=code)

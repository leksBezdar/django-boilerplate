from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.services.base import ISenderService


class DummySenderService(ISenderService):
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f"Code {code} was sent to user: {customer}")

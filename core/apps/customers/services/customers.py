from uuid import uuid4
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.exceptions.customers import InvalidCustomerTokenException
from core.apps.customers.models.customers import CustomerModel
from core.apps.customers.services.base import ICustomerService


class CustomerService(ICustomerService):
    def get_or_create_customer_by_phone(self, phone: str) -> CustomerEntity:
        customer_dto, _ = CustomerModel.objects.get_or_create(phone=phone)

        return customer_dto.to_entity()

    def get(self, phone: str) -> CustomerEntity:
        user_dto = CustomerModel.objects.get(phone=phone)

        return user_dto.to_entity()

    def generate_token(self, customer: CustomerEntity) -> str:
        new_token = str(uuid4())
        CustomerModel.objects.filter(phone=customer.phone).update(
            token=new_token,
        )

        return new_token

    def get_by_token(self, token: str) -> CustomerEntity | None:
        try:
            customer_dto = CustomerModel.objects.get(token=token)
        except CustomerModel.DoesNotExist:
            raise InvalidCustomerTokenException(token=token)

        return customer_dto.to_entity()

import random
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.customers.exceptions.codes import (
    CodeWasNotFoundException,
    CodesAreNotEqualException,
)
from core.apps.customers.services.base import ICodeSerivce
from django.core.cache import cache


class DjangoCacheCodeService(ICodeSerivce):
    def generate_code(self, customer: CustomerEntity) -> str:
        code = str(random.randint(10**5, 10**6 - 1))
        cache.set(customer.phone, code)

        return code

    def validate(self, code: str, customer: CustomerEntity) -> None:
        cached_code = cache.get(customer.phone)

        if cached_code is None:
            raise CodeWasNotFoundException(code=code)

        if cached_code != code:
            raise CodesAreNotEqualException(
                code=code, cached_code=cached_code, customer_phone=customer.phone
            )

        cache.delete(customer.phone)

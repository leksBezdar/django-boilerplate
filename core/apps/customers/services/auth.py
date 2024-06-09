from core.apps.customers.services.base import IAuthService


class AuthService(IAuthService):
    def authorize(self, phone: str):
        customer = self.customer_service.get_or_create_customer_by_phone(phone=phone)
        code = self.code_service.generate_code(customer=customer)
        self.sender_service.send_code(code=code)

    def confirm(self, code: str, phone: str):
        customer = self.customer_service.get(phone)
        self.code_service.validate(code=code, customer=customer)

        return self.customer_service.generate_token(customer=customer)

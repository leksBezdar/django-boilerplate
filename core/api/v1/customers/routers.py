from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import (
    ConfirmInSchema,
    ConfirmOutSchema,
    LoginInShema,
    LoginOutShema,
)
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import AuthService
from core.apps.customers.services.codes import DjangoCacheCodeService
from core.apps.customers.services.customers import CustomerService
from core.apps.customers.services.senders import DummySenderService


customer_router = Router(tags=["Customers"])


@customer_router.post(
    "login", response=ApiResponse[LoginOutShema], operation_id="login"
)
def login(request: HttpRequest, login_in: LoginInShema) -> ApiResponse[LoginOutShema]:
    auth_serivce = AuthService(
        customer_service=CustomerService(),
        code_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )
    auth_serivce.authorize(phone=login_in.phone)

    return ApiResponse(
        data=LoginOutShema(message=f"Code was sent to {login_in.phone}"),
    )


@customer_router.post(
    "confirm", response=ApiResponse[ConfirmOutSchema], operation_id="confirm"
)
def confirm(
    request: HttpRequest, confirm_in: ConfirmInSchema
) -> ApiResponse[ConfirmOutSchema]:
    auth_serivce = AuthService(
        customer_service=CustomerService(),
        code_service=DjangoCacheCodeService(),
        sender_service=DummySenderService(),
    )
    try:
        token = auth_serivce.confirm(code=confirm_in.code, phone=confirm_in.phone)

    except ServiceException as e:
        raise HttpError(status_code=400, message=e.message)

    return ApiResponse(data=ConfirmOutSchema(token=token))

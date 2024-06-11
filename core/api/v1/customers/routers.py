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
from core.apps.customers.services.base import IAuthService
from core.project.containers import init_container


customer_router = Router(tags=["Customers"])


@customer_router.post(
    "login", response={200: ApiResponse[LoginOutShema]}, operation_id="login"
)
def login(request: HttpRequest, login_in: LoginInShema) -> ApiResponse[LoginOutShema]:
    container = init_container()
    auth_service: IAuthService = container.resolve(IAuthService)

    auth_service.authorize(phone=login_in.phone)

    return ApiResponse(
        data=LoginOutShema(message=f"Code was sent to {login_in.phone}"),
    )


@customer_router.post(
    "confirm",
    response={
        200: ApiResponse[ConfirmOutSchema],
    },
    operation_id="confirm",
)
def confirm(
    request: HttpRequest, confirm_in: ConfirmInSchema
) -> ApiResponse[ConfirmOutSchema]:
    container = init_container()
    auth_service: IAuthService = container.resolve(IAuthService)

    try:
        token = auth_service.confirm(code=confirm_in.code, phone=confirm_in.phone)

    except ServiceException as e:
        raise HttpError(status_code=400, message=e.message)

    return ApiResponse(data=ConfirmOutSchema(token=token))

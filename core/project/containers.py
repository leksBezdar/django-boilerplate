from punq import Container
from functools import lru_cache

from core.apps.customers.services.auth import AuthService
from core.apps.customers.services.base import (
    IAuthService,
    ICodeSerivce,
    ICustomerService,
    ISenderService,
)
from core.apps.customers.services.codes import DjangoCacheCodeService
from core.apps.customers.services.customers import CustomerService
from core.apps.customers.services.senders import (
    ComposedSenderService,
    DummySenderService,
    EmailSenderService,
    PushSenderService,
)
from core.apps.products.services.base import (
    IProductReviewService,
    IProductReviewValidatorService,
    IProductService,
)
from core.apps.products.services.products import ProductService
from core.apps.products.services.reviews import (
    ComposedProductReviewValidatorService,
    ProductReviewService,
)
from core.apps.products.use_cases.reviews.create import CreateProductReviewUseCase


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # init services
    container.register(IProductService, ProductService)
    container.register(ICustomerService, CustomerService)
    container.register(ICodeSerivce, DjangoCacheCodeService)
    container.register(
        ISenderService,
        ComposedSenderService,
        sender_services=(
            DummySenderService(),
            EmailSenderService(),
            PushSenderService(),
        ),
    )
    container.register(IAuthService, AuthService)
    container.register(IProductReviewService, ProductReviewService)
    container.register(
        IProductReviewValidatorService,
        ComposedProductReviewValidatorService,
        list_validators=[],
    )
    container.register(CreateProductReviewUseCase)

    return container

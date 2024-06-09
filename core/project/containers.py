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
from core.apps.customers.services.senders import DummySenderService
from core.apps.products.services.base import IProductService
from core.apps.products.services.products import ProductService


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # init services
    container.register(IProductService, ProductService)
    container.register(ICustomerService, CustomerService)
    container.register(ICodeSerivce, DjangoCacheCodeService)
    container.register(ISenderService, DummySenderService)
    container.register(IAuthService, AuthService)

    return container

import pytest

from core.apps.products.services.base import IProductService
from core.apps.products.services.products import ProductService


@pytest.fixture
def product_service() -> IProductService:
    return ProductService()

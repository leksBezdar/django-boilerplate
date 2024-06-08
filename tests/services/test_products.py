import pytest
from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.models.products import ProductModel
from core.apps.products.services.base import IProductService
from tests.factories.products.products import ProductModelFactory


@pytest.mark.django_db
def test_get_products_count_eq_zero(product_service: IProductService):
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == 0, f"{products_count=}"


@pytest.mark.django_db
def test_get_products_count_exists(product_service: IProductService):
    expected_count = 5

    ProductModelFactory.create_batch(size=expected_count)
    products_count = product_service.get_product_count(ProductFilters())
    assert products_count == expected_count, f"{products_count=}"


@pytest.mark.django_db
def test_get_all_products(product_service: IProductService):
    expected_count = 5

    products: list[ProductModel] = ProductModelFactory.create_batch(size=expected_count)
    products_title = {product.title for product in products}

    fetched_products = product_service.get_product_list(
        ProductFilters(), PaginationIn()
    )
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f"{fetched_titles=}"
    assert fetched_titles == products_title, f"{fetched_titles=}"

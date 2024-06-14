from abc import ABC, abstractmethod
from typing import Iterable

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ProductReviewEntity


class IProductService(ABC):
    @abstractmethod
    def get_product_list(
        self, filters: ProductFilters, pagination: PaginationIn
    ) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int: ...

    @abstractmethod
    def get_by_id(self, product_id: int) -> ProductEntity: ...


class IProductReviewService(ABC):
    @abstractmethod
    def check_review_exists(
        self, product: ProductEntity, customer: CustomerEntity
    ) -> bool: ...

    @abstractmethod
    def save_review(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        review: ProductReviewEntity,
    ) -> ProductReviewEntity: ...


class IProductReviewValidatorService(ABC):
    @abstractmethod
    def validate(
        self,
        review: ProductReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ): ...

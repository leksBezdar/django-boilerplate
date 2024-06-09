from abc import ABC, abstractmethod
from typing import Iterable

from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.entities.products import ProductEntity


class IProductService(ABC):
    @abstractmethod
    def get_product_list(
        self, filters: ProductFilters, pagination: PaginationIn
    ) -> Iterable[ProductEntity]: ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int: ...

from typing import Iterable
from core.api.filters import PaginationIn
from core.apps.products.entities.products import ProductEntity
from core.apps.products.filters.products import ProductFiltersEntity
from core.apps.products.models.products import ProductModel
from core.apps.products.services.base import IProductService
from django.db.models import Q


class ProductService(IProductService):
    def _build_product_query(self, filters: ProductFiltersEntity) -> Q:
        query = Q(is_active=True)
        if filters.search is not None:
            query &= Q(title__icontains=filters.search) | Q(
                description__icontains=filters.search
            )

        return query

    def get_product_list(
        self, filters: ProductFiltersEntity, pagination: PaginationIn
    ) -> Iterable[ProductEntity]:
        query = self._build_product_query(filters)
        qs = ProductModel.objects.filter(query)[
            pagination.offset : pagination.offset + pagination.limit
        ]

        return [product.to_entity() for product in qs]

    def get_product_count(self, filters: ProductFiltersEntity) -> int:
        query = self._build_product_query(filters)

        return ProductModel.objects.filter(query).count()

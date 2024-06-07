from django.http import HttpRequest
from ninja import Query, Router

from core.api.filters import PaginationIn, PaginationOut
from core.api.schemas import ApiResponse, ListPaginatedResponse
from core.api.v1.products.filters import ProductFilters
from core.api.v1.products.schemas import SProduct
from core.apps.products.services.base import IProductService
from core.apps.products.services.products import ProductService


product_router = Router(tags=["Products"])


@product_router.get("", response=ApiResponse[ListPaginatedResponse[SProduct]])
def get_product_list(
    request: HttpRequest,
    pagination_in: Query[PaginationIn],
    filters: Query[ProductFilters],
) -> ApiResponse[ListPaginatedResponse[SProduct]]:
    service: IProductService = ProductService()
    product_list = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count = service.get_product_count(filters=filters)
    items = [SProduct.from_entity(obj) for obj in product_list]
    pagination_out = PaginationOut(
        offset=pagination_in.offset,
        limit=pagination_in.limit,
        total=product_count,
    )

    return ApiResponse(
        data=ListPaginatedResponse(items=items, pagination=pagination_out)
    )

from django.http import HttpRequest
from ninja import Router

from core.api.v1.products.schemas import SProductList


product_router = Router(tags=["Products"])


@product_router.get("", response=SProductList)
def get_product_list(request: HttpRequest) -> SProductList:
    return []

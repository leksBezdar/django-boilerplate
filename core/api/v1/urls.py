from ninja import Router

from core.api.v1.products.routers import product_router


v1_router = Router(tags=["v1"])


v1_router.add_router(prefix="products/", router=product_router)
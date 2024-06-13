from ninja import Router

from core.api.v1.products.routers import product_router
from core.api.v1.customers.routers import customer_router
from core.api.v1.reviews.routers import product_review_router


v1_router = Router(tags=["v1"])

product_router.add_router(prefix="", router=product_review_router)
v1_router.add_router(prefix="products/", router=product_router)
v1_router.add_router(prefix="auth/", router=customer_router)

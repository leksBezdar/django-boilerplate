from dataclasses import dataclass, field

from core.apps.common.enums import EntityStatus
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity


@dataclass
class ProductReviewEntity:
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: ProductEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default="")
    rating: int = field(default=1)

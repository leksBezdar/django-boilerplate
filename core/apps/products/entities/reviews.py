from dataclasses import dataclass, field
from datetime import datetime

from core.apps.common.entity_utils import utc_now
from core.apps.common.enums import EntityStatus
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity


@dataclass
class ProductReviewEntity:
    id: int | None = field(default=None, kw_only=True)
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: ProductEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default="")
    rating: int = field(default=1)

    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime | None = field(default=None)

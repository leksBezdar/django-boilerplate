from dataclasses import asdict
from datetime import datetime
from pydantic import BaseModel

from core.apps.products.entities.products import Product


class SProduct(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: Product) -> "SProduct":
        return SProduct(**asdict(entity))

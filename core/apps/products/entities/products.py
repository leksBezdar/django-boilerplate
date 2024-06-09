from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProductEntity:
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

from datetime import datetime
from pydantic import BaseModel


class SProduct(BaseModel):
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None
    is_active: bool


SProductList = list[SProduct]

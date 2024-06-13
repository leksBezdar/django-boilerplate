from dataclasses import asdict
from datetime import datetime
from pydantic import BaseModel

from core.apps.products.entities.reviews import ProductReviewEntity


class SProductReviewIn(BaseModel):
    rating: int
    text: str

    def to_entity(self):
        return ProductReviewEntity(
            text=self.text,
            rating=self.rating,
        )


class SCreateProductReview(BaseModel):
    review: SProductReviewIn

    product_id: int
    token: str


class SProductReviewOut(SProductReviewIn):
    id: int
    created_at: datetime
    updated_at: datetime | None

    def from_entity(entity: ProductReviewEntity) -> "SProductReviewOut":
        return SProductReviewOut(**asdict(entity))

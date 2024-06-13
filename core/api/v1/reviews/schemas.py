from datetime import datetime
from pydantic import BaseModel


class SProductReviewIn(BaseModel):
    rating: int
    text: str


class SCreateProductReview(BaseModel):
    review: SProductReviewIn

    product_id: int
    customer_id: int


class SProductReviewOut(SProductReviewIn):
    id: int
    created_at: datetime
    updated_at: datetime | None

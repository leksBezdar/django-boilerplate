from dataclasses import dataclass
from core.apps.products.exceptions.base import ProductReviewException


@dataclass(eq=False)
class InvaligProductReviewRatingException(ProductReviewException):
    rating: int

    @property
    def message(self):
        return f"Invalid rating for product review: {self.rating=}"


@dataclass(eq=False)
class CustomerAlreadyReviewedProductReviewException(ProductReviewException):
    customer_id: int
    product_id: int

    @property
    def message(self):
        return (
            f"Customer {self.customer_id=} already reviewed product {self.product_id=}"
        )

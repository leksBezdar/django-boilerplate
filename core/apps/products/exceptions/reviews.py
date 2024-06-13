from core.apps.products.exceptions.base import ProductReviewException


class InvaligProductReviewRatingException(ProductReviewException):
    rating: int

    @property
    def message(self):
        return f"Invalid rating for product review: {self.rating=}"

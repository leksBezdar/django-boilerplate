from dataclasses import dataclass

from core.apps.customers.services.base import ICustomerService
from core.apps.products.entities.reviews import ProductReviewEntity
from core.apps.products.services.base import (
    IProductReviewService,
    IProductService,
    IProductReviewValidatorService,
)


@dataclass
class CreateProductReviewUseCase:
    review_service: IProductReviewService
    customer_service: ICustomerService
    product_service: IProductService
    validator_service: IProductReviewValidatorService

    def execute(
        self,
        token: str,
        product_id: int,
        review: ProductReviewEntity,
    ) -> ProductReviewEntity:
        customer = self.customer_service.get_by_token(token=token)
        product = self.product_service.get_by_id(product_id=product_id)

        self.validator_service.validate(
            review=review, customer=customer, product=product
        )

        saved_review = self.review_service.save_review(
            product=product, customer=customer, review=review
        )

        return saved_review

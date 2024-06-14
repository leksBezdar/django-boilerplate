from dataclasses import dataclass
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ProductReviewEntity
from core.apps.products.exceptions.reviews import (
    CustomerAlreadyReviewedProductReviewException,
    InvaligProductReviewRatingException,
)
from core.apps.products.models.reviews import ProductReviewModel
from core.apps.products.services.base import (
    IProductReviewService,
    IProductReviewValidatorService,
)


class ProductReviewService(IProductReviewService):
    def check_review_exists(
        self, product: ProductEntity, customer: CustomerEntity
    ) -> bool:
        return ProductReviewModel.objects.filter(
            product_id=product.id,
            customer_id=customer.id,
        ).exists()

    def save_review(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        review: ProductReviewEntity,
    ) -> ProductReviewEntity:
        review_dto: ProductReviewModel = ProductReviewModel.from_entity(
            review=review, customer=customer, product=product
        )
        review_dto.save()
        return review_dto.to_entity()


class ProductReviewRatingValidatorService(IProductReviewValidatorService):
    def validate(
        self,
        review: ProductReviewEntity,
        *args,
        **kwargs,
    ):
        # TODO take out constants
        if review.rating not in range(1, 11):
            raise InvaligProductReviewRatingException(rating=review.rating)


@dataclass
class UniqueCustomerProductReviewValidatorService(IProductReviewValidatorService):
    review_service: IProductReviewService

    def validate(
        self,
        customer: CustomerEntity,
        product: ProductEntity,
        *args,
        **kwargs,
    ):
        if self.review_service.check_review_exists(product=product, customer=customer):
            raise CustomerAlreadyReviewedProductReviewException(
                customer_id=customer.id,
                product_id=product.id,
            )


@dataclass
class ComposedProductReviewValidatorService(IProductReviewValidatorService):
    list_validators: list[IProductReviewValidatorService]

    def validate(
        self,
        review: ProductReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ):
        for validator in self.list_validators:
            validator.validate(review=review, customer=customer, product=product)

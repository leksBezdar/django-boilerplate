from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities.customers import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ProductReviewEntity


class ProductReviewModel(TimedBaseModel):
    customer = models.ForeignKey(
        to="customers.CustomerModel",
        verbose_name="Reviewer",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to="products.ProductModel",
        verbose_name="Product",
        related_name="product_reviews",
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name="User rating",
        default=1,
    )
    text = models.TextField(
        verbose_name="Review text",
        blank=True,
        default="",
        max_length=1024,
    )

    # TODO get only review entity e.g.: review.product, review.customer
    @classmethod
    def from_entity(
        cls,
        review: ProductReviewEntity,
        product: ProductEntity,
        customer: CustomerEntity,
    ) -> "ProductReviewModel":
        return cls(
            pk=review.id,
            product_id=product.id,
            customer_id=customer.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(self) -> ProductReviewEntity:
        return ProductReviewEntity(
            text=self.text,
            rating=self.rating,
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product reviews"
        unique_together = ("customer", "product")

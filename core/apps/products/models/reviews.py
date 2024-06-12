from django.db import models

from core.apps.common.models import TimedBaseModel


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

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product reviews"
        unique_together = ("customer", "product")

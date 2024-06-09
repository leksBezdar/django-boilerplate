from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import ProductEntity


class ProductModel(TimedBaseModel):
    title = models.CharField(
        verbose_name="Product name",
        max_length=50,
    )
    description = models.TextField(verbose_name="Product description", blank=True)
    is_active = models.BooleanField(verbose_name="Product is active", default=True)

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.pk,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title

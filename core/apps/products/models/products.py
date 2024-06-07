from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product


class ProductModel(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название товара",
        max_length=50,
    )
    description = models.TextField(verbose_name="Описание товара", blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    def to_entity(self) -> Product:
        return Product(
            id=self.pk,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.title

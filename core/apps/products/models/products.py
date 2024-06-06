from django.db import models

from core.apps.common.models import TimedBaseModel


class Product(TimedBaseModel):
    title = models.CharField(
        verbose_name="Название товара",
        max_length=50,
    )
    description = models.TextField(verbose_name="Описание товара", blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.title

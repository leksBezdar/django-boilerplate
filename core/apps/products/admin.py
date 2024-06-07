from django.contrib import admin

from core.apps.products.models.products import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "is_active",
        "created_at",
        "updated_at",
    )

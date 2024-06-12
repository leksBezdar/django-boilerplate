from django.contrib import admin

from core.apps.products.models.products import ProductModel
from core.apps.products.models.reviews import ProductReviewModel


class ReviewProductInline(admin.TabularInline):
    model = ProductReviewModel
    extra = 0


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
    inlines = (ReviewProductInline,)


@admin.register(ProductReviewModel)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "product",
        "rating",
        "text",
        "created_at",
        "updated_at",
    )

    list_select_related = ("customer", "product")

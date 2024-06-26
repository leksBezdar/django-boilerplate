from django.contrib import admin

from core.apps.customers.models.customers import CustomerModel


@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "created_at",
    )
    search_fields = ("phone",)

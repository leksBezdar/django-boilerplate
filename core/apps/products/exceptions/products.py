from core.apps.products.exceptions.base import ProductException


class ProductNotFoundException(ProductException):
    product_id: int

    @property
    def message(self):
        return f"Product with id={self.product_id=} was not found"

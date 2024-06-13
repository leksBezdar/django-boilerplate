from dataclasses import dataclass
from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ProductException(ServiceException):
    @property
    def message(self):
        return "Product exception has occured"


@dataclass(eq=False)
class ProductReviewException(ProductException):
    @property
    def message(self):
        return "Product review exception has occured"

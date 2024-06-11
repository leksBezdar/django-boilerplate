from enum import Enum
from typing import (
    Any,
    Generic,
    TypeVar,
)

from ninja import Schema
from pydantic import Field

from core.api.filters import PaginationOut


TData = TypeVar("TData")
TListItem = TypeVar("TListItem")


class HealthStatus(Enum):
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"


class SHealthcheckOut(Schema):
    status: HealthStatus


class PingResponseSchema(Schema):
    result: bool


class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)

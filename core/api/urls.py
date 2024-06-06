from django.http import HttpRequest
from django.urls import path
from ninja import NinjaAPI

from core.api.schemas import SHealthcheckOut
from core.api.v1.urls import v1_router

api = NinjaAPI()


@api.get("/healthcheck", response=SHealthcheckOut)
def healthcheck(request: HttpRequest) -> SHealthcheckOut:
    return SHealthcheckOut(status="Healthy")


api.add_router(prefix="v1", router=v1_router)


urlpatterns = [
    path("", api.urls),
]

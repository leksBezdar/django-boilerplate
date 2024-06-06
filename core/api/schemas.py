from pydantic import BaseModel


class SHealthcheckOut(BaseModel):
    status: str = "Healthy"

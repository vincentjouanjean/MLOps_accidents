from pydantic import BaseModel


class PredictionDto(BaseModel):
    value: int

import uuid
from dataclasses import dataclass
from datetime import datetime

from domain import Accident


@dataclass
class AccidentPrediction:
    accident_id: uuid.UUID
    date: datetime.date
    prediction: bool
    version: str
    accident: Accident
    user: str
    def __init__(self, accident_id: uuid, date: datetime.date, prediction: bool, version: str, accident: Accident, user: str|None = None):
        super().__init__()
        self.accident_id = accident_id
        self.date = date
        self.prediction = prediction
        self.version = version
        self.accident = accident
        self.user = user

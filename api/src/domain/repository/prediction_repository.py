from abc import ABC, abstractmethod
from typing import List

from domain import AccidentPrediction


class PredictionRepository(ABC):

    @abstractmethod
    def save(self, accident_prediction: AccidentPrediction) -> AccidentPrediction:
        pass

    @abstractmethod
    def get_all(self) -> List[AccidentPrediction]:
        pass

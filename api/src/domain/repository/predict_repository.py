from abc import ABC, abstractmethod

from domain import Accident, AccidentPrediction


class PredictRepository(ABC):

    @abstractmethod
    def predict(self, accident: Accident) -> AccidentPrediction:
        pass

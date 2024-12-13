from typing import List

from domain import Accident, AccidentPrediction, PredictRepository, PredictionRepository


class PredictionService:
    def __init__(self, predict_repository: PredictRepository, prediction_repository: PredictionRepository):
        self.predict_repository = predict_repository
        self.prediction_repository = prediction_repository

    def predict(self, accident: Accident, user: str) -> AccidentPrediction:
        prediction = self.predict_repository.predict(accident)
        prediction.user = user
        self.prediction_repository.save(prediction)
        return prediction

    def get_all(self) -> List[AccidentPrediction]:
        return self.prediction_repository.get_all()

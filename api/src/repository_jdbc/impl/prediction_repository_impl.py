import os
from dataclasses import asdict
from typing import List

import pymongo

from domain import PredictionRepository, AccidentPrediction

DATABASE_CONNECTION = os.environ.get('DATABASE_CONNECTION', 'mongodb://mongodb:mongodb@localhost:27017')

client = pymongo.MongoClient(DATABASE_CONNECTION,
                             uuidRepresentation="pythonLegacy",
                             )
db = client.accident


class PredictionRepositoryImpl(PredictionRepository):

    def save(self, accident_prediction: AccidentPrediction) -> AccidentPrediction:
        db.accident_prediction.insert_one(asdict(accident_prediction))
        return accident_prediction

    def get_all(self) -> List[AccidentPrediction]:
        accident_predictions = []
        for accident_prediction in db.accident_prediction.find({}):
            del accident_prediction['_id']
            accident_predictions.append(AccidentPrediction(**accident_prediction))
        return accident_predictions

import os
import pickle
import uuid
from datetime import datetime

import redis
from sklearn import ensemble

from domain import PredictRepository, AccidentPrediction, Accident

REDIS_URL = os.environ.get('REDIS_URL', 'localhost')

redis = redis.StrictRedis(REDIS_URL)


class PredictRepositoryImpl(PredictRepository):

    def predict(self, accident: Accident) -> AccidentPrediction:
        version = redis.get('version')
        clf2: ensemble.RandomForestClassifier = pickle.loads(redis.get('accidents'))
        prediction = clf2.predict([[
            accident.place,
            accident.catu,
            accident.sexe,
            accident.secu1,
            accident.year_acc,
            accident.victim_age,
            accident.catv,
            accident.obsm,
            accident.motor,
            accident.catr,
            accident.circ,
            accident.surf,
            accident.situ,
            accident.vma,
            accident.jour,
            accident.mois,
            accident.lum,
            accident.dep,
            accident.com,
            accident.agg_,
            accident.int_,
            accident.atm,
            accident.col,
            accident.lat,
            accident.long,
            accident.hour,
            accident.nb_victim,
            accident.nb_vehicules
        ]])
        return AccidentPrediction(
            uuid.uuid4(),
            datetime.now(),
            prediction.tolist()[0] == 1,
            version,
            accident
        )

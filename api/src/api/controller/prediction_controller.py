import codecs
import os
from typing import Annotated, List

import requests
from authlib.oauth2.rfc9068 import JWTBearerTokenValidator
from fastapi import Depends, Request

from api import AccidentDto, PredictionDto
from domain import PredictionService, AccidentPrediction, Accident
from main import app
from repository_jdbc import PredictionRepositoryImpl
from repository_predict import PredictRepositoryImpl

prediction_service = PredictionService(PredictRepositoryImpl(),
                                       PredictionRepositoryImpl()
                                       )

ISS = os.environ.get('ISS', 'http://127.0.0.1:8000')
ISS_VALIDATE = os.environ.get('ISS', 'http://login-api:80')


class AccidentJWTBearerTokenValidator(JWTBearerTokenValidator):
    def get_jwks(self):
        response = requests.get(os.path.join(ISS, '.well-known/jwks.json'), timeout=2,
                                headers={"Content-Type": "application/json"})
        return response.json()


def get_current_user(
        request: Request,
):
    token = request.headers.get('Authorization')
    token_decode = AccidentJWTBearerTokenValidator.authenticate_token(
        AccidentJWTBearerTokenValidator(issuer=ISS_VALIDATE, resource_server=ISS_VALIDATE),
        codecs.encode(token)
    )
    AccidentJWTBearerTokenValidator.validate_token(
        AccidentJWTBearerTokenValidator(issuer=ISS_VALIDATE, resource_server=ISS_VALIDATE),
        token=token_decode,
        scopes=[],
        request='')
    return token_decode.get('sub')


@app.post("/predicts")
async def predicts(
        accident_dto: AccidentDto,
        current_user: Annotated[str, Depends(get_current_user)]
) -> PredictionDto:
    predict: AccidentPrediction = prediction_service.predict(Accident(
        accident_dto.place,
        accident_dto.catu,
        accident_dto.sexe,
        accident_dto.secu1,
        accident_dto.year_acc,
        accident_dto.victim_age,
        accident_dto.catv,
        accident_dto.obsm,
        accident_dto.motor,
        accident_dto.catr,
        accident_dto.circ,
        accident_dto.surf,
        accident_dto.situ,
        accident_dto.vma,
        accident_dto.jour,
        accident_dto.mois,
        accident_dto.lum,
        accident_dto.dep,
        accident_dto.com,
        accident_dto.agg_,
        accident_dto.int_,
        accident_dto.atm,
        accident_dto.col,
        accident_dto.lat,
        accident_dto.long,
        accident_dto.hour,
        accident_dto.nb_victim,
        accident_dto.nb_vehicules,

    ), current_user)
    return PredictionDto(value=predict.prediction)


@app.get("/predictions")
async def predictions(
        current_user: Annotated[str, Depends(get_current_user)]
) -> List:
    return prediction_service.get_all()

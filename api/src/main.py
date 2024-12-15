from fastapi import FastAPI
from prometheus_client import make_asgi_app

app = FastAPI()

from api import prediction_controller

# Add prometheus asgi middleware to route /metrics requests
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

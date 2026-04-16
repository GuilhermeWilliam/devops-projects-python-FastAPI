from fastapi import FastAPI
import requests
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()
REQUEST_COUNT = Counter(
    "gateway_requests_total",
    "Total requests to gateway"
)
DATA_SERVICE_URL = "http://data-service:3001/data"
AUTHOR_SERVICE_URL = "http://data-service:3001/author"

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    try:
        data = requests.get(DATA_SERVICE_URL, timeout=3).json()
    except requests.exceptions.RequestException:
        data = {"error": "data-service unreachable"}

    try:
        author = requests.get(AUTHOR_SERVICE_URL, timeout=3).json()
    except requests.exceptions.RequestException:
        author = {"error": "author-service unreachable"}

    return {
        "gateway_message": "Hello from gateway-service",
        "data_service_response": data,
        "author_service_response": author
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()
REQUEST_COUNT = Counter(
    "data_service_requests_total",
    "Total requests to data service"
)

@app.get("/data")
def get_data():
    REQUEST_COUNT.inc()
    return {
        "message": "Hello from data-service",
        "items": ["apple", "banana", "orange"]
    }

@app.get("/author")
def get_author():
    REQUEST_COUNT.inc()
    return {
        "name": "Guilherme L. Joao",
        "title": "MsC Telecom, Senior QA Engineer"
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
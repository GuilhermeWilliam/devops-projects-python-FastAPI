from fastapi import FastAPI
import requests

app = FastAPI()

DATA_SERVICE_URL = "http://data-service:3001/data"
AUTHOR_SERVICE_URL = "http://data-service:3001/author"

@app.get("/")
def root():
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
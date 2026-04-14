from fastapi import FastAPI

app = FastAPI()

@app.get("/data")
def get_data():
    return {
        "message": "Hello from data-service",
        "items": ["apple", "banana", "orange"]
    }

@app.get("/author")
def get_author():
    return {
        "name": "Guilherme L. Joao",
        "title": "MsC Telecom, Senior QA Engineer"
    }
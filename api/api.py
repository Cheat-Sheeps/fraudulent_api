import json
from fastapi import FastAPI
from pydantic import BaseModel
from ai_model.fraudulent_website_detector import FraudulentWebsiteDetector

class PredictRequest(BaseModel):
    words: list[str]

app = FastAPI()
fraudulentWebsiteDetector = FraudulentWebsiteDetector()

@app.post("/predict")
async def root(request: PredictRequest):
    print(request)
    page_content = " ".join(request.words)
    print(page_content)
    result = fraudulentWebsiteDetector.predict(request.words)
    print(result.tolist())
    return (result.tolist())

@app.get("/metrics/total_queries")
async def total_queries():
    return { "data": [{
        "value": 100,
        "name": "Total queries",
        "time": "2021-10-20T12:00:00Z",
    }, {
        "value": 200,
        "name": "Total queries",
        "time": "2021-10-20T12:01:00Z",
    }, {
        "value": 300,
        "name": "Total queries",
        "time": "2021-10-20T12:02:00Z",
    }]}

@app.get("/metrics/number_blacklist")
async def number_blacklist():
    return { "data": [{
        "value": 100,
        "name": "Number of blacklisted websites",
        "time": "2021-10-20T12:00:00Z",
    }, {
        "value": 200,
        "name": "Number of blacklisted websites",
        "time": "2021-10-20T12:01:00Z",
    }, {
        "value": 300,
        "name": "Number of blacklisted websites",
        "time": "2021-10-20T12:02:00Z",
    }]}

@app.get("/metrics/pourcentage_phishing")
async def pourcentage_phishing():
    return { "data": [{
        "value": 0.1,
        "name": "Pourcentage of phishing websites",
        "time": "2021-10-20T12:00:00Z",
    }, {
        "value": 0.2,
        "name": "Pourcentage of phishing websites",
        "time": "2021-10-20T12:01:00Z",
    }, {
        "value": 1.18,
        "name": "Pourcentage of phishing websites",
        "time": "2021-10-20T12:02:00Z",
    }]}


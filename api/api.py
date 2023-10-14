from datetime import datetime
import json
from fastapi import FastAPI
from pydantic import BaseModel
from ai_model.fraudulent_website_detector import FraudulentWebsiteDetector
from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload

client = PocketBase("http://localhost:8090")

admin_data = client.admins.auth_with_password("theodorelheureux@gmail.com", "vpCDk1%cP@Q#Htp@")

class PredictRequest(BaseModel):
    words: list[str]
    url: str

app = FastAPI()
fraudulentWebsiteDetector = FraudulentWebsiteDetector()

@app.post("/predict")
async def root(request: PredictRequest):
    result = fraudulentWebsiteDetector.predict(request.words)
    print(result.tolist())

    domain_name = request.url.split("//")[1].split("/")[0]

    data = {
        "url": request.url,
        "domain_name": domain_name,
        "is_phishing": result.tolist()[0][0] > 0.5
    };

    res = client.collection("Query").create(data)
    return (result.tolist())

@app.get("/metrics/total_queries")
async def total_queries():
    count = client.collection("Query").get_list(
    1, 20).total_items

    return { "data": [{
        "value": count,
        "name": "Total queries",
        "time": "2021-10-20T12:00:00Z",
    }]}

@app.get("/metrics/number_blacklist")
async def number_blacklist():
    count = client.collection("Blacklist").get_list(
    1, 20).total_items

    return { "data": [{
        "value": count,
        "name": "Number of blacklisted websites",
        "time": "2021-10-20T12:00:00Z",
    }]}

@app.get("/metrics/number_phishing_query")
async def percent_phishing_query():
    count_phishing = client.collection("Query").get_list(
    1, 20, {"filter": 'is_phishing = true'}).total_items
    count_total = client.collection("Query").get_list(
    1, 20).total_items
    percentage = count_phishing / count_total * 100

    return { "data": [{
        "value": percentage,
        "name": "Pourcentage of phishing queries",
        "time": datetime.now().isoformat(),
    }]}

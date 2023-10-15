from datetime import datetime, timedelta
import json
from fastapi import FastAPI
from pydantic import BaseModel
from ai_model.fraudulent_website_detector import FraudulentWebsiteDetector
from pocketbase import PocketBase  # Client also works the same
from fastapi.middleware.cors import CORSMiddleware
from pocketbase.client import FileUpload
import statistics

client = PocketBase("http://localhost:8090")

admin_data = client.admins.auth_with_password("theodorelheureux@gmail.com", "vpCDk1%cP@Q#Htp@")

class PredictRequest(BaseModel):
    words: list[str]
    url: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fraudulentWebsiteDetector = FraudulentWebsiteDetector()

@app.post("/predict")
async def root(request: PredictRequest):
    domain = request.url.split("//")[1].split("/")[0]

    is_blacklisted = client.collection("Blacklist").get_list(
    1, 20, {"filter": 'domain = "' + domain + '"'}).total_items > 0
    is_whitelisted = client.collection("Whitelist").get_list(
    1, 20, {"filter": 'domain = "' + domain + '"'}).total_items > 0

    if request.words == []:
        return { "data": {
            "result": [],
            "is_phishing": False,
            "is_blacklisted": is_blacklisted,
            "is_whitelisted": is_whitelisted,
            "median": 0,
        }}
    
    if len(request.words) > 50:
        request.words = request.words[:50]

    result = fraudulentWebsiteDetector.predict(request.words)
    result_flat = [item for sublist in result.tolist() for item in sublist]
    median = statistics.median(result_flat)

    data = {
        "url": request.url,
        "domain": domain,
        "is_phishing": median > 0.5,
    }

    client.collection("Query").create(data)


    return { "data": {
        "result": result.tolist(),
        "is_phishing": median > 0.5,
        "is_blacklisted": is_blacklisted,
        "is_whitelisted": is_whitelisted,
        "median": median,
    }}

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
async def number_phishing_query():
    count = client.collection("Query").get_list(
    1, 20, {"filter": 'is_phishing = true'}).total_items

    return { "data": [{
        "value": count,
        "name": "Number of phishing queries",
        "time": "2021-10-20T12:00:00Z",
    }]}

@app.get("/metrics/pourcentage_phishing")
async def percent_phishing_query():
    count_phishing = client.collection("Query").get_list(
    1, 20, {"filter": 'is_phishing = true'}).total_items
    count_total = client.collection("Query").get_list(
    1, 20).total_items
    percentage = round(count_phishing / count_total * 100, 2)

    return { "data": [{
        "value": percentage,
        "name": "Pourcentage of phishing queries",
        "time": datetime.now().isoformat(),
    }]}

@app.get("/metrics/detected_phishing_last_12h")
async def detected_phishing_last_12h():
    count = []
    n_hours = 12

    for i in range(n_hours):
        lowest_date = (datetime.utcnow() - timedelta(hours=i+1)).strftime("%Y-%m-%d %H:%M:%S")
        highest_date = (datetime.utcnow() - timedelta(hours=i)).strftime("%Y-%m-%d %H:%M:%S")

        print(lowest_date)
        print(highest_date)

        result = client.collection("Query").get_list(
        1, 20, {"filter": 'is_phishing = true && created > "' + lowest_date + '" && created < "' + highest_date + '"'})
        print(result)
        print("\n\n\n\n")
        count.append(result.total_items)

    res = []

    for i in range(n_hours):
        res.append({
            "value": count[i],
            "name": "Number of phishing queries",
            "time": (datetime.utcnow() - timedelta(hours=i)).isoformat(),
        })

    # send data array with 12 objects with value and time
    return { "data": res}
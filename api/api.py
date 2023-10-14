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
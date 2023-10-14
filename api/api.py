from fastapi import FastAPI
from a

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import milk as milk
import pandas as pd

class api_data(BaseModel):
    pH: float
    Temprature: int
    Taste: int
    Odor: int
    Fat: int
    Turbidity: int  
    Colour: int

app = FastAPI()

@app.get("/")
def home():
    return "Hello, FastAPI up!"

@app.post("/predict-grade/")
def predict(data: api_data):
    return {"grade": milk.predict_grade(data)}

if __name__ == "__main__":
    uvicorn.run("api:app", host = "0.0.0.0", port = 8080)
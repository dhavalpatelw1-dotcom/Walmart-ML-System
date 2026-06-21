from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.predict import predict_sales

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputData(BaseModel):

    Store: int
    Holiday_Flag: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    Year: int
    Month: int
    Week: int
    Quarter: int
    Lag1: float
    Lag2: float
    Lag3: float
    Rolling_Mean: float



@app.get("/")
def home():
    return {"msg": "API running"}


@app.post("/predict")
def predict(data: InputData):

    result = predict_sales(data.dict())

    return {
        "prediction": result
    }
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="House Price Predictor API",
    description="Predicts house prices based on features",
    version="1.0.0"
)

try:
    model = joblib.load('house_price_model.jb')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None

class PredictionRequest(BaseModel):
    OverallQual: float
    GrLivArea: float
    GarageCars: float
    FirstFlrSF: float
    TotBath: float
    YearBuilt: float
    YearRemodAdd: float
    MasVnrArea: float
    Fireplaces: float
    BsmtFinSF1: float
    LotFrontage: float
    WoodDeckSF: float
    OpenPorchSF: float
    LotArea: float
    CentralAir: str

@app.post("/predict")
def predict(request: PredictionRequest):
    """Make a house price prediction"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="House Price Predictor API",
    description="Predicts house prices based on features",
    version="1.0.0"
)

MODEL_PATH = "house_price_model.jb"

try:
    model = joblib.load(MODEL_PATH)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    model = None


class PredictionRequest(BaseModel):
    OverallQual: float
    GrLivArea: float
    GarageArea: float
    FirstFlrSF: float  # maps to '1stFlrSF' — Python names can't start with a digit
    FullBath: float
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


class PredictionResponse(BaseModel):
    predicted_price: float


@app.get("/")
def root():
    return {"status": "ok", "message": "House Price Predictor API is running"}


@app.get("/health")
def health():
    return {"status": "ok" if model is not None else "model not loaded"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """Make a house price prediction"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded")

    try:
        central_air = 1.0 if request.CentralAir.strip().upper() == "Y" else 0.0

        # NOTE: this order MUST match the column order used when the model was trained.
        features = np.array([[
    request.OverallQual,
    request.GrLivArea,
    request.GarageArea,
    request.FirstFlrSF,
    request.FullBath,
    request.YearBuilt,
    request.YearRemodAdd,
    request.MasVnrArea,
    request.Fireplaces,
    request.BsmtFinSF1,
    request.LotFrontage,
    request.WoodDeckSF,
    request.OpenPorchSF,
    request.LotArea,
    central_air,
]])

        prediction = model.predict(features)[0]
        return PredictionResponse(predicted_price=round(float(prediction), 2))

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# 🏠 House Price Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-teal)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

A machine learning web app that predicts house sale prices from property features, served through both a **Streamlit UI** and a **FastAPI REST endpoint**, containerized with Docker.

**🔗 Live demo:** [house-price-prediction9.streamlit.app](https://house-price-prediction9.streamlit.app/)

![Demo Preview](https://img.shields.io/badge/status-live-brightgreen)

---

## What this does

Given details about a house — square footage, quality rating, garage size, year built, and more — the app predicts its likely sale price using a regression model trained on housing data (Ames-style feature set).

Two ways to use it:
- **Web app** — fill in a form, click predict, get a price instantly.
- **REST API** — `POST /predict` with a JSON payload, get a price back for integration into other tools.

## Tech stack

| Layer | Tool |
|---|---|
| Model training | scikit-learn, pandas (see `notebook.ipynb`) |
| Model serving (API) | FastAPI, Pydantic |
| Web UI | Streamlit |
| Model persistence | joblib |
| Containerization | Docker |

## Project structure

```
├── notebook.ipynb          # EDA, feature engineering, model training
├── app.py                  # Streamlit web app
├── api.py                  # FastAPI REST endpoint
├── house_price_model.jb    # Trained model (joblib)
├── dataset.csv             # Training data
├── Dockerfile
└── requirements.txt
```

## Running locally

```bash
git clone https://github.com/kunalsharmadev/House-Price-Prediction.git
cd House-Price-Prediction
pip install -r requirements.txt
```

**Streamlit app:**
```bash
streamlit run app.py
```

**FastAPI server:**
```bash
uvicorn api:app --reload
```

**With Docker:**
```bash
docker build -t house-price-predictor .
docker run -p 8000:8000 house-price-predictor
```

## API usage

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "OverallQual": 7,
    "GrLivArea": 1710,
    "GarageCars": 2,
    "FirstFlrSF": 856,
    "TotBath": 2,
    "YearBuilt": 2003,
    "YearRemodAdd": 2003,
    "MasVnrArea": 196,
    "Fireplaces": 0,
    "BsmtFinSF1": 706,
    "LotFrontage": 65,
    "WoodDeckSF": 0,
    "OpenPorchSF": 61,
    "LotArea": 8450,
    "CentralAir": "Y"
  }'
```

> Response: `{"predicted_price": <value>}`

## Model

Trained in `notebook.ipynb` on 15 property features (quality rating, living area, garage capacity, basement finish, lot size, year built/remodeled, and more). See the notebook for the full EDA, feature selection, and evaluation metrics.

## Roadmap

- [ ] Align feature names/units between the API and Streamlit inputs
- [ ] Add input validation ranges and error handling for out-of-range values
- [ ] Add model evaluation metrics (RMSE, R²) to this README
- [ ] Add automated tests for the API endpoint
- [ ] CI pipeline for build/test on push

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

[Kunal Sharma](https://github.com/kunalsharmadev)

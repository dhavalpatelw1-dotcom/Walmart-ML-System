import numpy as np
from app.model_loader import get_model

model = get_model()


def predict_sales(data):

    features = np.array([[
        data["Store"],
        data["Holiday_Flag"],
        data["Temperature"],
        data["Fuel_Price"],
        data["CPI"],
        data["Unemployment"],
        data["Year"],
        data["Month"],
        data["Week"],
        data["Quarter"],
        data["Lag1"],
        data["Lag2"],
        data["Lag3"],
        data["Rolling_Mean"]
    ]])

    pred = model.predict(features)

    return float(pred[0])
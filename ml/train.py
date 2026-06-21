import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("../data/Walmart_Store_sales.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Week"] = df["Date"].dt.isocalendar().week.astype(int)
df["Quarter"] = df["Date"].dt.quarter

df = df.sort_values(["Store", "Date"])

df["Lag1"] = df.groupby("Store")["Weekly_Sales"].shift(1)
df["Lag2"] = df.groupby("Store")["Weekly_Sales"].shift(2)

df["Rolling_Mean"] = (
    df.groupby("Store")["Weekly_Sales"]
    .rolling(4)
    .mean()
    .reset_index(0, drop=True)
)

df = df.dropna()

features = [
    "Store","Holiday_Flag","Temperature","Fuel_Price",
    "CPI","Unemployment","Year","Month","Week",
    "Quarter","Lag1","Lag2","Rolling_Mean"
]

X = df[features]
y = df["Weekly_Sales"]

model = RandomForestRegressor(n_estimators=300)

model.fit(X, y)

pickle.dump(
    model,
    open("../model/walmart_best_model.pkl", "wb")
)

print("Model saved")
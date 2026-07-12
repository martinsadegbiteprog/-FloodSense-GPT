import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample synthetic dataset (replace with real Lagos data later)
data = pd.DataFrame({
    "rainfall": [20, 50, 80, 120, 150, 200],
    "discharge": [50, 100, 200, 300, 400, 500],
    "soil_moisture": [0.2, 0.4, 0.6, 0.8, 0.9, 1.0],
    "flood_risk": [0.1, 0.3, 0.5, 0.7, 0.85, 0.95]
})

X = data[["rainfall", "discharge", "soil_moisture"]]
y = data["flood_risk"]

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "../backend/model/flood_model.pkl")
print("Model saved ✅")

import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("crop_yield_with_temp.csv")
df = df[df['Crop'].str.lower() == 'rice'].copy()
df.dropna(inplace=True)

# Select features (excluding Production)
X = df[['Crop_Year', 'Area', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Temperature']]
y = df['Yield']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
rf = RandomForestRegressor(n_estimators=100, random_state=42)
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)

# Train models
rf.fit(X_train, y_train)
gbr.fit(X_train, y_train)

# Evaluate
rf_r2 = r2_score(y_test, rf.predict(X_test))
gbr_r2 = r2_score(y_test, gbr.predict(X_test))

print(f"Random Forest R² Score: {rf_r2:.4f}")
print(f"Gradient Boosting R² Score: {gbr_r2:.4f}")

# Select better model
best_model = rf if rf_r2 > gbr_r2 else gbr
chosen_name = "Random Forest" if rf_r2 > gbr_r2 else "Gradient Boosting"

# Save model
os.makedirs("model", exist_ok=True)
with open("model/rice_yield_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print(f"✅ {chosen_name} model saved to model/rice_yield_model.pkl")

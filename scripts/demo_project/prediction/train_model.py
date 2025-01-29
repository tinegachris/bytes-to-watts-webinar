import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load data
solar_df = pd.read_csv("data/solar_generation.csv")
energy_df = pd.read_csv("data/energy_consumption.csv")

# Merge datasets on timestamp
solar_df['timestamp'] = pd.to_datetime(solar_df['timestamp'])
energy_df['timestamp'] = pd.to_datetime(energy_df['timestamp'])
data = pd.merge(solar_df, energy_df, on='timestamp')

# Feature engineering
data['hour'] = data['timestamp'].dt.hour
data['day_of_week'] = data['timestamp'].dt.dayofweek
data['month'] = data['timestamp'].dt.month
data.drop(columns=['timestamp'], inplace=True)

# Define features and target
X = data[['hour', 'day_of_week', 'month', 'solar_generation_kW']]
y = data['energy_consumption_kW']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Performance: MAE={mae:.2f}, R2={r2:.2f}")

# Save trained model
with open("data/forecast_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model trained and saved successfully.")

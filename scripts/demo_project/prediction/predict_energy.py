import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta

# Load trained model
model = joblib.load('data/forecast_model.pkl')

# Generate future timestamps for prediction (next 24 hours, every 15 minutes)
future_timestamps = [datetime.now() + timedelta(minutes=15*i) for i in range(96)]

# Create feature set for prediction (e.g., time-based features)
def create_features(timestamps):
    return pd.DataFrame({
        'hour': [t.hour for t in timestamps],
        'day_of_week': [t.weekday() for t in timestamps],
        'month': [t.month for t in timestamps]
    })

future_features = create_features(future_timestamps)

# Make predictions
predicted_energy = model.predict(future_features)

# Store results in a DataFrame
predictions_df = pd.DataFrame({'timestamp': future_timestamps, 'predicted_energy_kW': predicted_energy})

# Save predictions to CSV
predictions_df.to_csv('data/predicted_energy.csv', index=False)

print("Future energy predictions saved in 'data/predicted_energy.csv'")
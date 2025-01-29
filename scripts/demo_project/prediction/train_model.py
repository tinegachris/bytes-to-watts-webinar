import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib

# Load data
solar_data = pd.read_csv('scripts/demo_project/data/solar_generation.csv')
energy_data = pd.read_csv('scripts/demo_project/data/energy_consumption.csv')
battery_data = pd.read_csv('scripts/demo_project/data/battery_status.csv')

# Merge data on timestamp
data = pd.merge(solar_data, energy_data, on='timestamp')
data = pd.merge(data, battery_data, on='timestamp')

# Create features and target
data['hour'] = pd.to_datetime(data['timestamp']).dt.hour
data['day_of_week'] = pd.to_datetime(data['timestamp']).dt.weekday
data['month'] = pd.to_datetime(data['timestamp']).dt.month
features = data[['hour', 'day_of_week', 'month', 'solar_generation_kW', 'battery_status_%']]
target = data['energy_consumption_kW']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Save model
joblib.dump(model, 'scripts/demo_project/data/forecast_model.pkl')
print("Model saved as 'scripts/demo_project/data/forecast_model.pkl'")

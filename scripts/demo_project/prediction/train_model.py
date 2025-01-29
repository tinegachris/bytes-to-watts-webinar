import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
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

# Hyperparameter tuning using GridSearchCV
param_grid = {
  'n_estimators': [100, 200, 300],
  'max_depth': [None, 10, 20, 30],
  'min_samples_split': [2, 5, 10],
  'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=RandomForestRegressor(random_state=42), param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Train model with best parameters
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Evaluate model
predictions = best_model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Save model
joblib.dump(best_model, 'scripts/demo_project/data/forecast_model.pkl')
print("Model saved as 'scripts/demo_project/data/forecast_model.pkl'")

import os

# Define paths for data files
data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
SOLAR_DATA_FILE = os.path.join(data_dir, "solar_generation.csv")
ENERGY_DATA_FILE = os.path.join(data_dir, "energy_consumption.csv")
BATTERY_DATA_FILE = os.path.join(data_dir, "battery_status.csv")
FORECAST_MODEL_FILE = os.path.join(data_dir, "forecast_model.pkl")

# Battery settings
BATTERY_CAPACITY_KWH = 5000  # Total capacity in kWh
BATTERY_MIN_CHARGE = 10  # Minimum charge level (%)
BATTERY_MAX_CHARGE = 100  # Maximum charge level (%)

# Load prioritization settings
CRITICAL_LOAD_THRESHOLD = 800  # kW threshold for critical loads
LOAD_SHEDDING_THRESHOLD = 20  # Battery % below which load shedding occurs

# Optimization settings
OPTIMIZATION_INTERVAL = 15  # Optimization check interval in minutes

# Visualization settings
PLOT_REFRESH_INTERVAL = 5  # Seconds between plot refreshes in live monitoring

# API settings (for real-time data streaming, if applicable)
API_ENDPOINT = "http://localhost:5000/data"  # Placeholder for live API endpoint

print("Configuration settings loaded.")

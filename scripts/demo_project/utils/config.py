from pathlib import Path

# Define paths for data files
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SOLAR_DATA_FILE = DATA_DIR / "solar_generation.csv"
ENERGY_DATA_FILE = DATA_DIR / "energy_consumption.csv"
BATTERY_DATA_FILE = DATA_DIR / "battery_status.csv"
FORECAST_MODEL_FILE = DATA_DIR / "forecast_model.pkl"

# Battery settings
BATTERY_CAPACITY_KWH: int = 5000  # Total capacity in kWh
BATTERY_MIN_CHARGE: int = 10  # Minimum charge level (%)
BATTERY_MAX_CHARGE: int = 100  # Maximum charge level (%)

# Load prioritization settings
CRITICAL_LOAD_THRESHOLD: int = 800  # kW threshold for critical loads
LOAD_SHEDDING_THRESHOLD: int = 20  # Battery % below which load shedding occurs

# Optimization settings
OPTIMIZATION_INTERVAL: int = 15  # Optimization check interval in minutes

# Visualization settings
PLOT_REFRESH_INTERVAL: int = 5  # Seconds between plot refreshes in live monitoring

# API settings (for real-time data streaming, if applicable)
API_ENDPOINT: str = "http://localhost:5000/data"  # Placeholder for live API endpoint

print("Configuration settings loaded.")

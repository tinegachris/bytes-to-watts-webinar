import pandas as pd
import time
import random
from datetime import datetime

# Function to simulate real-time data streaming
def stream_data():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        solar_generation = max(0, random.uniform(0, 1000))  # Simulating solar power
        energy_consumption = random.uniform(200, 1000)  # Simulating load consumption
        battery_status = random.uniform(10, 100)  # Simulating battery charge status
        
        # Print the simulated data (replace with actual streaming logic if needed)
        print(f"{timestamp}, Solar: {solar_generation:.2f} kW, Load: {energy_consumption:.2f} kW, Battery: {battery_status:.2f} %")
        
        # Simulate a delay (e.g., 5 seconds between updates)
        time.sleep(5)

if __name__ == "__main__":
    stream_data()
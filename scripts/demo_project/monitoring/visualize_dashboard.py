import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
solar_df = pd.read_csv('scripts/demo_project/data/solar_generation.csv')
energy_df = pd.read_csv('scripts/demo_project/data/energy_consumption.csv')
battery_df = pd.read_csv('scripts/demo_project/data/battery_status.csv')

# Convert timestamps to datetime objects
solar_df['timestamp'] = pd.to_datetime(solar_df['timestamp'])
energy_df['timestamp'] = pd.to_datetime(energy_df['timestamp'])
battery_df['timestamp'] = pd.to_datetime(battery_df['timestamp'])

# Plot the data
plt.figure(figsize=(12, 8))
plt.plot(solar_df['timestamp'], solar_df['solar_generation_kW'], label='Solar Generation (kW)', color='orange')
plt.plot(energy_df['timestamp'], energy_df['energy_consumption_kW'], label='Energy Consumption (kW)', color='blue')
plt.plot(battery_df['timestamp'], battery_df['battery_status_%'], label='Battery Status (%)', color='green')

# Formatting
plt.title('Real-time Energy Monitoring Dashboard')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()

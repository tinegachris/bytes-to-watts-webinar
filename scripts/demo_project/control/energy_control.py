import pandas as pd

# Load generated data
solar_df = pd.read_csv('scripts/demo_project/data/solar_generation.csv')
energy_df = pd.read_csv('scripts/demo_project/data/energy_consumption.csv')
battery_df = pd.read_csv('scripts/demo_project/data/battery_status.csv')

# Merge datasets on timestamp
solar_df['timestamp'] = pd.to_datetime(solar_df['timestamp'])
energy_df['timestamp'] = pd.to_datetime(energy_df['timestamp'])
battery_df['timestamp'] = pd.to_datetime(battery_df['timestamp'])

data = solar_df.merge(energy_df, on='timestamp').merge(battery_df, on='timestamp')

# Initialize system parameters
battery_capacity = 5000  # kWh
critical_battery_level = 20  # %
control_actions = []

for i in range(len(data)):
    net_power = data.loc[i, 'solar_generation_kW'] - data.loc[i, 'energy_consumption_kW']
    battery_charge = data.loc[i, 'battery_status_%']

    if net_power > 0:  # Excess power, charge battery
        action = "Charging"
    elif net_power < 0 and battery_charge > critical_battery_level:  # Discharge battery if not critical
        action = "Discharging"
    elif battery_charge <= critical_battery_level:  # Critical battery level, activate load shedding
        action = "Load Shedding"
    else:
        action = "No Action"

    control_actions.append(action)

# Add control actions to data and save
data['control_action'] = control_actions
data.to_csv('scripts/demo_project/data/controlled_energy_data.csv', index=False)

print("Energy control logic executed and data saved in 'scripts/demo_project/data/controlled_energy_data.csv'.")
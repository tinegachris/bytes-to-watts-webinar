import pandas as pd
import numpy as np

# Load data
def load_data():
    solar_df = pd.read_csv("data/solar_generation.csv")
    energy_df = pd.read_csv("data/energy_consumption.csv")
    battery_df = pd.read_csv("data/battery_status.csv")
    return solar_df, energy_df, battery_df

# Optimization function
def optimize_energy_usage(solar_df, energy_df, battery_df, battery_capacity=5000):
    optimized_actions = []
    battery_charge = battery_df["battery_status_%"].iloc[0]
    
    for i in range(len(solar_df)):
        net_power = solar_df["solar_generation_kW"].iloc[i] - energy_df["energy_consumption_kW"].iloc[i]
        
        if net_power > 0:  # Excess power
            if battery_charge < 100:
                battery_charge = min(100, battery_charge + (net_power / battery_capacity) * 100)
                optimized_actions.append("Charging")
            else:
                optimized_actions.append("Export to Grid")
        elif net_power < 0:  # Deficit
            discharge_power = min(abs(net_power), (battery_charge / 100) * battery_capacity)
            if discharge_power > 0:
                battery_charge = max(0, battery_charge - (discharge_power / battery_capacity) * 100)
                optimized_actions.append("Discharging")
            else:
                optimized_actions.append("Load Shedding")
        else:
            optimized_actions.append("No Action")
    
    return optimized_actions

# Main execution
if __name__ == "__main__":
    solar_df, energy_df, battery_df = load_data()
    optimized_actions = optimize_energy_usage(solar_df, energy_df, battery_df)
    
    # Save optimized actions
    battery_df["optimized_action"] = optimized_actions
    battery_df.to_csv("data/battery_optimized.csv", index=False)
    print("Optimization complete. Results saved in 'data/battery_optimized.csv'.")
import pandas as pd
import os

def load_csv_data(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Parameters:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} not found.")
        return None
    
    return pd.read_csv(file_path, parse_dates=['timestamp'])

def load_all_data(data_dir="data"):
    """
    Load all required energy data files into DataFrames.
    
    Parameters:
        data_dir (str): Directory containing data files.
    
    Returns:
        dict: Dictionary containing all loaded DataFrames.
    """
    data_files = {
        "solar": os.path.join(data_dir, "solar_generation.csv"),
        "energy": os.path.join(data_dir, "energy_consumption.csv"),
        "battery": os.path.join(data_dir, "battery_status.csv")
    }
    
    data = {key: load_csv_data(path) for key, path in data_files.items()}
    return data

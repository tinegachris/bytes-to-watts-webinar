import pandas as pd
import os
import logging
from typing import Optional, Dict

logging.basicConfig(level=logging.INFO)

def load_csv_data(file_path: str, parse_dates: Optional[list] = None) -> Optional[pd.DataFrame]:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.
        parse_dates (list, optional): List of columns to parse as dates.

    Returns:
        Optional[pd.DataFrame]: Loaded data as a DataFrame or None if file not found.
    """
    if not os.path.exists(file_path):
        logging.warning(f"{file_path} not found.")
        return None

    try:
        return pd.read_csv(file_path, parse_dates=parse_dates)
    except Exception as e:
        logging.error(f"Error loading {file_path}: {e}")
        return None

def load_all_data(data_dir: str = "data") -> Dict[str, Optional[pd.DataFrame]]:
    """
    Load all required energy data files into DataFrames.

    Parameters:
        data_dir (str): Directory containing data files.

    Returns:
        Dict[str, Optional[pd.DataFrame]]: Dictionary containing all loaded DataFrames.
    """
    data_files = {
        "solar": os.path.join(data_dir, "solar_generation.csv"),
        "energy": os.path.join(data_dir, "energy_consumption.csv"),
        "battery": os.path.join(data_dir, "battery_status.csv")
    }

    data = {key: load_csv_data(path, parse_dates=['timestamp']) for key, path in data_files.items()}
    return data

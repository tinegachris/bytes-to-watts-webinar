import pandas as pd
from pathlib import Path
import logging
from typing import Optional, Dict, List

logging.basicConfig(level=logging.INFO)

def load_csv_data(file_path: str, parse_dates: Optional[List[str]] = None) -> Optional[pd.DataFrame]:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file.
        parse_dates (list, optional): List of columns to parse as dates.

    Returns:
        Optional[pd.DataFrame]: Loaded data as a DataFrame or None if file not found.
    """
    path = Path(file_path)
    if not path.exists():
        logging.warning(f"File not found: {file_path}")
        return None

    try:
        return pd.read_csv(file_path, parse_dates=parse_dates)
    except Exception as e:
        logging.error(f"Error loading file {file_path}: {e}")
        return None

def load_all_data(data_dir: str = "data") -> Dict[str, Optional[pd.DataFrame]]:
    """
    Load all required energy data files into DataFrames.

    Parameters:
        data_dir (str): Directory containing data files.

    Returns:
        Dict[str, Optional[pd.DataFrame]]: Dictionary containing all loaded DataFrames.
    """
    data_dir_path = Path(data_dir)
    data_files = {
        "solar": data_dir_path / "solar_generation.csv",
        "energy": data_dir_path / "energy_consumption.csv",
        "battery": data_dir_path / "battery_status.csv"
    }

    data = {key: load_csv_data(str(path), parse_dates=['timestamp']) for key, path in data_files.items()}
    return data

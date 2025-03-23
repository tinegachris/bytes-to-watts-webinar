# Energy Prediction Demo Project

This demo project is part of the Bytes to Watts webinar series. It demonstrates various concepts and techniques for energy consumption prediction and optimization.

## Project Structure

```
demo_project/
├── data/                   # Data files directory
│   ├── solar_generation.csv
│   ├── energy_consumption.csv
│   ├── battery_status.csv
│   └── predicted_energy.csv
├── prediction/            # Prediction module
│   ├── train_model.py    # Model training script
│   └── predict_energy.py # Energy prediction script
├── control/              # Control module
├── monitoring/           # Monitoring module
├── optimization/         # Optimization module
├── utils/               # Utility functions
├── templates/           # Template files
└── requirements.txt     # Project dependencies
```

## Features

- Time-series data generation for energy consumption
- Solar generation prediction
- Battery status monitoring
- Energy consumption forecasting
- Model training and evaluation
- Data visualization

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Train the model:
```bash
python prediction/train_model.py
```

2. Generate predictions:
```bash
python prediction/predict_energy.py
```

## Data Format

The project uses CSV files with the following structure:

- `solar_generation.csv`: Solar power generation data
- `energy_consumption.csv`: Energy consumption data
- `battery_status.csv`: Battery status information
- `predicted_energy.csv`: Model predictions

Each CSV file contains:
- `timestamp`: DateTime of the measurement
- `value`: Measured value in appropriate units (kW, %, etc.)

## Model Details

The project uses a Random Forest Regressor for energy consumption prediction with the following features:
- Hour of day
- Day of week
- Month
- Solar generation
- Battery status

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

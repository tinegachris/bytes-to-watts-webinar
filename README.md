# Bytes to Watts Webinar

![bytes-to-watts-webinar](https://github.com/user-attachments/assets/b08f805e-50bb-4779-bf0d-a30a470c6abf)

Welcome to the Bytes to Watts Webinar. This repository contains all the materials related to the webinar, including slides, scripts, resources, images, notes, and Q&A.

## Contents

- `slides/`: Presentation slides
- `scripts/`: Example code snippets or demos
  - `data/`: Sample or real-time data files
    - `solar_generation.csv`: Simulated solar power generation data
    - `energy_consumption.csv`: Simulated load consumption data
    - `battery_status.csv`: Simulated battery charge/discharge levels
    - `forecast_model.pkl`: Saved ML model for predictions (optional)
  - `monitoring/`: Data visualization and real-time monitoring scripts
    - `visualize_dashboard.py`: Displays live solar, battery, and load data
    - `stream_data.py`: Simulates real-time data streaming
  - `control/`: Scripts for system control logic
    - `energy_control.py`: Basic rule-based control system
    - `manual_control.py`: Interactive CLI/web-based toggle for energy devices
  - `optimization/`: Energy optimization algorithms
    - `optimize_usage.py`: Load prioritization & battery management algorithm
  - `prediction/`: Forecasting energy generation and consumption
    - `train_model.py`: ML model training script
    - `predict_energy.py`: Predicts future energy usage and solar generation
  - `utils/`: Helper functions for data processing
    - `data_loader.py`: Reads and preprocesses CSV or API data
    - `config.py`: Stores system settings and constants
  - `pyproject.toml`: Dependencies and project configuration
  - `README.md`: Explanation of scripts and how to run the demo
- `resources/`: Related articles, papers, and documentation
- `images/`: Diagrams, charts, or visuals used in the presentation
- `Q&A/`: Collected questions and answers from the webinar

## Getting Started

To get started with the demo project, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/tinegachris/bytes-to-watts-webinar.git
    cd bytes-to-watts-webinar/scripts
    ```

2. Install the required dependencies using Poetry:

    ```sh
    pip install poetry
    poetry install
    ```

3. Run the real-time dashboard:

    ```sh
    streamlit run monitoring/visualize_dashboard.py
    ```

## Project Overview

### Smart Solar Monitoring

The smart solar monitoring project demonstrates how to optimize solar energy usage using simulated data. It includes the following components:

- **Data**: Simulated historical and real-time solar energy data.
- **Dashboard**: A Streamlit-based real-time dashboard to visualize energy data.
- **Optimization**: Scripts to optimize energy usage.
- **Prediction**: Modules to predict future energy generation and consumption.

### Utility Scripts

The utility scripts include helper functions for data manipulation and visualization, making it easier to preprocess data and create charts or graphs.

## Resources

Check the `resources/` directory for related articles, papers, and documentation that provide additional context and information about the topics covered in the webinar.

## Contributing

We welcome contributions to improve the project. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork.
5. Open a pull request to the main repository.

## Contact

For any questions or feedback, please open an issue in this repository.

Thank you for participating in the Bytes to Watts Webinar!

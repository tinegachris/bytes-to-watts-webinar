import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
import logging
from typing import Tuple, Dict, Any, Optional
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EnergyModelTrainer:
    def __init__(self, data_dir: str = 'data'):
        """
        Initialize the EnergyModelTrainer.

        Args:
            data_dir: Directory containing the training data files
        """
        self.data_dir = data_dir
        self.model: Optional[RandomForestRegressor] = None
        self.best_params: Optional[Dict[str, Any]] = None

    def load_data(self) -> pd.DataFrame:
        """
        Load and merge all required data files.

        Returns:
            Merged DataFrame containing all features and target
        """
        try:
            # Load individual data files
            solar_data = pd.read_csv(os.path.join(self.data_dir, 'solar_generation.csv'))
            energy_data = pd.read_csv(os.path.join(self.data_dir, 'energy_consumption.csv'))
            battery_data = pd.read_csv(os.path.join(self.data_dir, 'battery_status.csv'))

            # Merge data on timestamp
            data = pd.merge(solar_data, energy_data, on='timestamp')
            data = pd.merge(data, battery_data, on='timestamp')

            # Convert timestamp to datetime
            data['timestamp'] = pd.to_datetime(data['timestamp'])

            return data

        except Exception as e:
            logger.error(f"Failed to load data: {str(e)}")
            raise

    def prepare_features(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Prepare features and target for model training.

        Args:
            data: DataFrame containing raw data

        Returns:
            Tuple of (features DataFrame, target Series)
        """
        # Create time-based features
        data['hour'] = data['timestamp'].dt.hour
        data['day_of_week'] = data['timestamp'].dt.weekday
        data['month'] = data['timestamp'].dt.month

        # Select features and target
        features = data[['hour', 'day_of_week', 'month', 'solar_generation_kW', 'battery_status_%']]
        target = data['energy_consumption_kW']

        return features, target

    def train_model(self, test_size: float = 0.2, random_state: int = 42) -> None:
        """
        Train the energy prediction model using GridSearchCV.

        Args:
            test_size: Proportion of data to use for testing
            random_state: Random seed for reproducibility
        """
        try:
            # Load and prepare data
            data = self.load_data()
            features, target = self.prepare_features(data)

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                features, target, test_size=test_size, random_state=random_state
            )

            # Define hyperparameter grid
            param_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            }

            # Perform grid search
            grid_search = GridSearchCV(
                estimator=RandomForestRegressor(random_state=random_state),
                param_grid=param_grid,
                cv=3,
                n_jobs=-1,
                verbose=2
            )

            logger.info("Starting grid search...")
            grid_search.fit(X_train, y_train)

            # Store best model and parameters
            self.model = grid_search.best_estimator_
            self.best_params = grid_search.best_params_

            # Evaluate model
            self._evaluate_model(X_test, y_test)

        except Exception as e:
            logger.error(f"Failed to train model: {str(e)}")
            raise

    def _evaluate_model(self, X_test: pd.DataFrame, y_test: pd.Series) -> None:
        """
        Evaluate the trained model on test data.

        Args:
            X_test: Test features
            y_test: Test target
        """
        if self.model is None:
            raise ValueError("Model not trained yet")

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logger.info(f"Model Performance:")
        logger.info(f"Mean Squared Error: {mse:.4f}")
        logger.info(f"R² Score: {r2:.4f}")
        logger.info(f"Best Parameters: {self.best_params}")

    def save_model(self, model_path: Optional[str] = None) -> None:
        """
        Save the trained model to disk.

        Args:
            model_path: Path to save the model. If None, uses default path.
        """
        try:
            if self.model is None:
                raise ValueError("No trained model available to save")

            model_path = model_path or os.path.join(self.data_dir, 'forecast_model.pkl')
            joblib.dump(self.model, model_path)
            logger.info(f"Model saved to {model_path}")

        except Exception as e:
            logger.error(f"Failed to save model: {str(e)}")
            raise

def main():
    """Main function to train and save the model."""
    try:
        trainer = EnergyModelTrainer()
        trainer.train_model()
        trainer.save_model()
    except Exception as e:
        logger.error(f"Failed to complete training process: {str(e)}")
        raise

if __name__ == "__main__":
    main()

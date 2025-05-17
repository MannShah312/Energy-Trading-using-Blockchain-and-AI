import pandas as pd
from prophet import Prophet
from utils.data_preprocessing import preprocess_generation_data, preprocess_weather_data, merge_datasets
from models.metrics import calculate_metrics

class SolarGenerationModel:
    def __init__(self, generation_data_path="data/hourly_solar_generation.csv", 
                 weather_data_path="data/weather_hourly_data.csv"):
        """
        Initialize the SolarGenerationModel with dataset paths.

        Parameters:
            generation_data_path (str): Path to the solar generation dataset.
            weather_data_path (str): Path to the weather dataset.
        """
        self.generation_data_path = generation_data_path
        self.weather_data_path = weather_data_path
        self.model = None
        self.merged_data = None
        self._initialize_model()

    def _initialize_model(self):
        """Load and preprocess data, and initialize the Prophet model."""
        try:
            # Preprocess datasets
            generation_data = preprocess_generation_data(self.generation_data_path)
            weather_data = preprocess_weather_data(self.weather_data_path)
            self.merged_data = merge_datasets(generation_data, weather_data)

            # Initialize Prophet model and add regressors
            self.model = Prophet(daily_seasonality=True, yearly_seasonality=True)
            self.model.add_regressor('temperature')
            self.model.add_regressor('humidity')
            self.model.add_regressor('dew_point')
            self.model.add_regressor('wind_speed')

            # Train the model
            self.model.fit(self.merged_data)
        except Exception as e:
            raise ValueError(f"Error initializing SolarGenerationModel: {str(e)}")

    def predict(self, forecast_hours=24):
        """
        Predict solar generation for the next specified hours.

        Parameters:
            forecast_hours (int): Number of hours to forecast.

        Returns:
            list: A list of dictionaries containing the forecast.
        """
        try:
            # Get the last timestamp from the dataset
            last_date = self.merged_data['ds'].max()

            # Create a DataFrame for the future predictions
            future_dates = pd.date_range(start=last_date + pd.Timedelta(hours=1), 
                                         periods=forecast_hours, freq='h')
            future_df = pd.DataFrame({'ds': future_dates})

            # Use the last known weather data for future predictions
            last_weather = self.merged_data[['temperature', 'humidity', 'dew_point', 'wind_speed']].iloc[-1]
            for col in ['temperature', 'humidity', 'dew_point', 'wind_speed']:
                future_df[col] = last_weather[col]

            # Make predictions
            forecast = self.model.predict(future_df)

            # Set nighttime predictions (18:00 to 06:00) to zero
            forecast.loc[(forecast['ds'].dt.hour < 6) | (forecast['ds'].dt.hour >= 18), 'yhat'] = 0

            # Return predictions as a list of dictionaries
            return forecast[['ds', 'yhat']].to_dict(orient='records')
        except Exception as e:
            raise ValueError(f"Error during prediction: {str(e)}")

    def calculate_metrics(self):
        """
        Calculate evaluation metrics for the model using test data.

        Returns:
            dict: A dictionary containing the evaluation metrics.
        """
        try:
            # Split the dataset into train and test sets
            train_size = int(0.8 * len(self.merged_data))
            train_data = self.merged_data.iloc[:train_size]
            test_data = self.merged_data.iloc[train_size:]

            # Train a model on the training set
            train_model = Prophet(daily_seasonality=True, yearly_seasonality=True)
            train_model.add_regressor('temperature')
            train_model.add_regressor('humidity')
            train_model.add_regressor('dew_point')
            train_model.add_regressor('wind_speed')
            train_model.fit(train_data)

            # Make predictions for the test set
            future_test = test_data[['ds', 'temperature', 'humidity', 'dew_point', 'wind_speed']]
            forecast_test = train_model.predict(future_test)


            # Calculate metrics
            actual = test_data['y']
            predicted = forecast_test['yhat']
            return calculate_metrics(actual, predicted)
        except Exception as e:
            raise ValueError(f"Error calculating metrics: {str(e)}")
import pandas as pd

def preprocess_generation_data(file_path):
    """
    Preprocess the solar generation data.

    Parameters:
        file_path (str): Path to the solar generation dataset.

    Returns:
        pd.DataFrame: Preprocessed generation data.
    """
    try:
        generation_data = pd.read_csv(file_path)
        generation_data['datetime'] = pd.to_datetime(
            generation_data['date'] + ' ' + generation_data['time'],
            format='%d-%m-%Y %H:%M:%S',
            errors='raise'
        )
        generation_data = generation_data.rename(columns={
            'datetime': 'ds',
            'hourly_generation (kWh)': 'y'
        })
        return generation_data[['ds', 'y']]
    except Exception as e:
        raise ValueError(f"Error preprocessing generation data: {str(e)}")

def preprocess_weather_data(file_path):
    """
    Preprocess the weather data.

    Parameters:
        file_path (str): Path to the weather dataset.

    Returns:
        pd.DataFrame: Preprocessed weather data.
    """
    try:
        weather_data = pd.read_csv(file_path)
        weather_data['datetime'] = pd.to_datetime(
            weather_data['date'] + ' ' + weather_data['time'],
            format='%d-%m-%Y %H:%M',
            errors='raise'
        )
        weather_data = weather_data.rename(columns={
            'datetime': 'ds',
            'temperature': 'temperature',
            'relative_humidity': 'humidity',
            'dew_point': 'dew_point',
            'wind_speed': 'wind_speed'
        })
        return weather_data[['ds', 'temperature', 'humidity', 'dew_point', 'wind_speed']]
    except Exception as e:
        raise ValueError(f"Error preprocessing weather data: {str(e)}")

def merge_datasets(generation_data, weather_data):
    """
    Merge the solar generation and weather datasets on the 'ds' column.

    Parameters:
        generation_data (pd.DataFrame): Preprocessed solar generation data.
        weather_data (pd.DataFrame): Preprocessed weather data.

    Returns:
        pd.DataFrame: Merged dataset.
    """
    try:
        merged_data = pd.merge(
            generation_data,
            weather_data,
            on='ds',
            how='left'
        )
        return merged_data
    except Exception as e:
        raise ValueError(f"Error merging datasets: {str(e)}")
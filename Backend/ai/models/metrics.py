from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
import numpy as np

def calculate_metrics(actual, predicted):
    """
    Calculate evaluation metrics for the model.

    Parameters:
        actual (list or np.ndarray): Actual values.
        predicted (list or np.ndarray): Predicted values.

    Returns:
        dict: A dictionary containing MAE, MAPE, and RMSE.
    """
    try:
        mae = mean_absolute_error(actual, predicted)
        mape = mean_absolute_percentage_error(actual, predicted) * 100  # Convert to percentage
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        
        return {
            "Mean Absolute Error (MAE)": mae,
            "Mean Absolute Percentage Error (MAPE)": mape,
            "Root Mean Square Error (RMSE)": rmse
        }
    except Exception as e:
        raise ValueError(f"Error calculating metrics: {str(e)}")
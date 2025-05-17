# # # from flask import Flask, request, jsonify
# # # from models.solar_generation_model import SolarGenerationModel

# # # app = Flask(__name__)

# # # # Initialize the model
# # # solar_model = SolarGenerationModel()

# # # @app.route('/predict', methods=['POST'])
# # # def predict():
# # #     """API endpoint to predict solar generation."""
# # #     try:
# # #         forecast_hours = int(request.json.get('forecast_hours', 24))
# # #         forecast = solar_model.predict(forecast_hours)
# # #         return jsonify({"status": "success", "forecast": forecast}), 200
# # #     except Exception as e:
# # #         return jsonify({"status": "error", "message": str(e)}), 500

# # # @app.route('/metrics', methods=['GET'])
# # # def metrics():
# # #     """API endpoint to calculate model metrics."""
# # #     try:
# # #         metrics = solar_model.calculate_metrics()
# # #         return jsonify({"status": "success", "metrics": metrics}), 200
# # #     except Exception as e:
# # #         return jsonify({"status": "error", "message": str(e)}), 500


# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # from flask import Flask, jsonify, request
# # from flask_cors import CORS
# # from models.solar_generation_model import SolarGenerationModel

# # # Initialize the Flask app
# # app = Flask(__name__)

# # # Enable CORS for cross-origin requests
# # CORS(app)

# # # Load the Solar Generation Model
# # solar_model = SolarGenerationModel()

# # @app.route('/', methods=['GET'])
# # def home():
# #     """
# #     API Home Endpoint
# #     """
# #     return jsonify({"message": "Welcome to the Solar Generation Forecast API!"})


# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     """
# #     Predict solar generation for the next specified hours.

# #     Request Body:
# #         {
# #             "forecast_hours": 24  # Number of hours to forecast (default: 24)
# #         }

# #     Response:
# #         {
# #             "forecast": [
# #                 {"ds": "2024-12-06 07:00:00", "yhat": 10.5},
# #                 {"ds": "2024-12-06 08:00:00", "yhat": 12.3},
# #                 ...
# #             ]
# #         }
# #     """
# #     try:
# #         # Parse forecast_hours from the request (default to 24 if not provided)
# #         forecast_hours = int(request.json.get('forecast_hours', 24))

# #         # Get predictions from the SolarGenerationModel
# #         forecast = solar_model.predict(forecast_hours)

# #         return jsonify({"forecast": forecast}), 200
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500


# # @app.route('/metrics', methods=['GET'])
# # def metrics():
# #     """
# #     Calculate and return evaluation metrics for the model.

# #     Response:
# #         {
# #             "metrics": {
# #                 "mae": 5.3,
# #                 "mape": 12.7,
# #                 "rmse": 6.1
# #             }
# #         }
# #     """
# #     try:
# #         # Get metrics from the SolarGenerationModel
# #         metrics = solar_model.calculate_metrics()

# #         return jsonify({"metrics": metrics}), 200
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500


# # if __name__ == '__main__':
# #     # Run the Flask app
# #     app.run(debug=True, host='0.0.0.0', port=5000)


# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from models.solar_generation_model import SolarGenerationModel

# app = Flask(__name__)
# CORS(app)

# # Load the Solar Generation Model
# model = SolarGenerationModel()

# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     try:
# #         # Get forecast_hours from request body
# #         forecast_hours = request.json.get('forecast_hours', 24)
        
# #         # Get predictions from the model
# #         predictions = model.predict(forecast_hours)
        
# #         # Format predictions as a list of dictionaries
# #         formatted_predictions = [
# #             {"date": p["date"], "hour": p["hour"], "generation": p["generation"]}
# #             for p in predictions
# #         ]
        
# #         # Return predictions
# #         return jsonify(formatted_predictions), 200
# #     except Exception as e:
# #         return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Log the incoming data
#         app.logger.info("Received request data: %s", request.json)

#         # Get forecast_hours from the request
#         forecast_hours = request.json.get('forecast_hours', 24)
#         app.logger.info("Forecast hours: %d", forecast_hours)

#         # Get predictions from the model
#         predictions = model.predict(forecast_hours)
#         app.logger.info("Raw predictions: %s", predictions)

#         # Format predictions as a list of dictionaries
#         formatted_predictions = [
#             {"date": p["ds"].strftime("%Y-%m-%d"),  # Format the 'ds' field
#              "hour": p["ds"].hour,                 # Extract hour from 'ds'
#              "generation": p["yhat"]}             # Map 'yhat' to 'generation'
#             for p in predictions
#         ]
#         app.logger.info("Formatted predictions: %s", formatted_predictions)

#         # Return predictions
#         return jsonify(formatted_predictions), 200

#     except Exception as e:
#         app.logger.error("Error in /predict: %s", str(e))
#         return jsonify({"error": f"Prediction failed: {str(e)}"}), 500
    
    

# @app.route('/metrics', methods=['GET'])
# def metrics():
#     try:
#         # Fetch metrics from the model
#         model_metrics = model.get_metrics()
        
#         # Return metrics
#         return jsonify(model_metrics), 200
#     except Exception as e:
#         return jsonify({"error": f"Metrics retrieval failed: {str(e)}"}), 500
# if __name__ == '__main__':
#     app.run(debug=True, port=5000)


# import os
# import csv
# from flask import Flask, request, jsonify
# from models.solar_generation_model import SolarGenerationModel


# app = Flask(__name__)

# # Initialize the model
# model = SolarGenerationModel()

# # Directory to save CSV files
# CSV_DIR = "daily_predictions"
# os.makedirs(CSV_DIR, exist_ok=True)  # Create directory if it doesn't exist

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Log incoming request data
#         app.logger.info("Received request data: %s", request.json)

#         # Extract forecast_hours from request body
#         forecast_hours = request.json.get('forecast_hours', 24)
#         app.logger.info("Forecast hours: %d", forecast_hours)

#         # Get predictions from the model
#         predictions = model.predict(forecast_hours)
#         app.logger.info("Raw predictions: %s", predictions)

#         # Format predictions into a list of dictionaries
#         formatted_predictions = [
#             {
#                 "date": p["ds"].strftime("%Y-%m-%d"),  # Format date as string
#                 "hour": p["ds"].hour,                 # Extract hour from datetime
#                 "generation": p["yhat"]              # Use yhat as generation
#             }
#             for p in predictions
#         ]
#         app.logger.info("Formatted predictions: %s", formatted_predictions)

#         # Save predictions to a CSV file
#         csv_filename = os.path.join(CSV_DIR, f"predictions_{formatted_predictions[0]['date']}.csv")
#         with open(csv_filename, mode='w', newline='') as csv_file:
#             writer = csv.DictWriter(csv_file, fieldnames=["date", "hour", "generation"])
#             writer.writeheader()  # Write column headers
#             writer.writerows(formatted_predictions)  # Write prediction rows
#         app.logger.info("Predictions saved to: %s", csv_filename)

#         # Return predictions as JSON response
#         return jsonify({"message": "Predictions fetched successfully", "predictions": formatted_predictions}), 200

#     except Exception as e:
#         app.logger.error("Error in /predict: %s", str(e))
#         return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

# if __name__ == "__main__":
#     app.run(debug=True)

# import os
# import csv
# from flask import Flask, request, jsonify
# from models.solar_generation_model import SolarGenerationModel
# import pandas as pd
# from datetime import datetime

# app = Flask(__name__)

# # Initialize the model
# model = SolarGenerationModel()

# # Directory to save CSV files
# CSV_DIR = "daily_predictions"
# os.makedirs(CSV_DIR, exist_ok=True)  # Create directory if it doesn't exist

# # Directory to save data files (e.g., consumption, weather)
# DATA_DIR = "data"
# os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if it doesn't exist

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Log incoming request data
#         app.logger.info("Received request data: %s", request.json)

#         # Extract forecast_hours from request body
#         forecast_hours = request.json.get('forecast_hours', 24)
#         app.logger.info("Forecast hours: %d", forecast_hours)

#         # Get predictions from the model
#         predictions = model.predict(forecast_hours)
#         app.logger.info("Raw predictions: %s", predictions)

#         # Format predictions into a list of dictionaries
#         formatted_predictions = [
#             {
#                 "date": p["ds"].strftime("%Y-%m-%d"),  # Format date as string
#                 "hour": p["ds"].hour,                 # Extract hour from datetime
#                 "generation": p["yhat"]              # Use yhat as generation
#             }
#             for p in predictions
#         ]
#         app.logger.info("Formatted predictions: %s", formatted_predictions)

#         # Save predictions to a CSV file
#         csv_filename = os.path.join(CSV_DIR, f"predictions_{formatted_predictions[0]['date']}.csv")
#         with open(csv_filename, mode='w', newline='') as csv_file:
#             writer = csv.DictWriter(csv_file, fieldnames=["date", "hour", "generation"])
#             writer.writeheader()  # Write column headers
#             writer.writerows(formatted_predictions)  # Write prediction rows
#         app.logger.info("Predictions saved to: %s", csv_filename)

#         # Return predictions as JSON response
#         return jsonify({"message": "Predictions fetched successfully", "predictions": formatted_predictions}), 200

#     except Exception as e:
#         app.logger.error("Error in /predict: %s", str(e))
#         return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


# @app.route('/consumption/current', methods=['GET'])
# def get_current_consumption():
#     try:
#         # Current date and hour
#         now = datetime.now()
#         current_date = now.strftime('%Y-%m-%d')
#         current_hour = now.hour

#         # Path to the consumption file
#         csv_path = os.path.join(DATA_DIR, "consumption_data.csv")

#         # Check if the file exists
#         if not os.path.exists(csv_path):
#             return jsonify({"error": "Consumption file not found"}), 404

#         # Load consumption data
#         data = pd.read_csv(csv_path)

#         # Filter data for current date and hour
#         filtered_data = data[
#             (data['date'] == current_date) & 
#             (data['hour'] == current_hour)
#         ]

#         # If no data is found, return an empty response
#         if filtered_data.empty:
#             return jsonify({"message": "No data found for the current time"}), 200

#         # Convert data to a dictionary format for response
#         result = filtered_data.to_dict(orient='records')[0]

#         return jsonify({
#             "message": "Consumption data fetched successfully",
#             "data": result
#         }), 200

#     except Exception as e:
#         app.logger.error("Error in /consumption/current: %s", str(e))
#         return jsonify({"error": f"Error fetching consumption data: {str(e)}"}), 500


# if __name__ == "__main__":
#     app.run(debug=True)


# import os
# import csv
# from flask import Flask, request, jsonify
# from models.solar_generation_model import SolarGenerationModel
# import pandas as pd
# from datetime import datetime

# app = Flask(__name__)

# # Initialize the model
# model = SolarGenerationModel()

# # Directory to save CSV files
# CSV_DIR = "daily_predictions"
# os.makedirs(CSV_DIR, exist_ok=True)  # Create directory if it doesn't exist

# # Directory to save data files (e.g., consumption, weather)
# DATA_DIR = "data"
# os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if it doesn't exist

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Log incoming request data
#         app.logger.info("Received request data: %s", request.json)

#         # Extract forecast_hours from request body
#         forecast_hours = request.json.get('forecast_hours', 24)
#         app.logger.info("Forecast hours: %d", forecast_hours)

#         # Get predictions from the model
#         predictions = model.predict(forecast_hours)
#         app.logger.info("Raw predictions: %s", predictions)

#         # Format predictions into a list of dictionaries
#         formatted_predictions = [
#             {
#                 "date": p["ds"].strftime("%Y-%m-%d"),  # Format date as string
#                 "hour": p["ds"].hour,                 # Extract hour from datetime
#                 "generation": p["yhat"]              # Use yhat as generation
#             }
#             for p in predictions
#         ]
#         app.logger.info("Formatted predictions: %s", formatted_predictions)

#         # Save predictions to a CSV file
#         csv_filename = os.path.join(CSV_DIR, f"predictions_{formatted_predictions[0]['date']}.csv")
#         with open(csv_filename, mode='w', newline='') as csv_file:
#             writer = csv.DictWriter(csv_file, fieldnames=["date", "hour", "generation"])
#             writer.writeheader()  # Write column headers
#             writer.writerows(formatted_predictions)  # Write prediction rows
#         app.logger.info("Predictions saved to: %s", csv_filename)

#         # Return predictions as JSON response
#         return jsonify({"message": "Predictions fetched successfully", "predictions": formatted_predictions}), 200

#     except Exception as e:
#         app.logger.error("Error in /predict: %s", str(e))
#         return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


# @app.route('/consumption/current', methods=['GET'])
# def get_current_consumption():
#     try:
#         # Current date and hour
#         now = datetime.now()
#         current_date = now.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
#         current_hour = now.hour  # Get current hour

#         # Path to the consumption file
#         csv_path = os.path.join(DATA_DIR, "consumption_data.csv")

#         # Check if the file exists
#         if not os.path.exists(csv_path):
#             return jsonify({"error": "Consumption file not found"}), 404

#         # Load consumption data using pandas
#         data = pd.read_csv(csv_path)

#         # Log the current date and hour for debugging
#         app.logger.info(f"Current Date: {current_date}, Current Hour: {current_hour}")

#         # Assuming the 'hour' column has time in 'hh:mm:ss' format, 
#         # we need to extract the hour part from the time string.
#         data['hour'] = data['hour'].apply(lambda x: int(x.split(':')[0]))  # Extract the hour from 'hh:mm:ss'

#         # Log the first few rows of data to ensure it's loaded correctly
#         app.logger.info(f"Data Preview:\n{data.head()}")

#         # Filter data for current date and hour
#         filtered_data = data[
#             (data['date'] == current_date) & 
#             (data['hour'] == current_hour)
#         ]

#         # Log the filtered data to check if it matches the current time
#         app.logger.info(f"Filtered Data:\n{filtered_data}")

#         # If no data is found, return an empty response
#         if filtered_data.empty:
#             return jsonify({"message": "No data found for the current time"}), 200

#         # Convert the first matching row to a dictionary
#         result = filtered_data.iloc[0].to_dict()

#         return jsonify({
#             "message": "Consumption data fetched successfully",
#             "data": result
#         }), 200

#     except Exception as e:
#         app.logger.error("Error in /consumption/current: %s", str(e))
#         return jsonify({"error": f"Error fetching consumption data: {str(e)}"}), 500



# if __name__ == "__main__":
#     app.run(debug=True)


import os
import csv
from flask import Flask, request, jsonify
from models.solar_generation_model import SolarGenerationModel
import pandas as pd
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# Initialize the model
model = SolarGenerationModel()

# Directory to save CSV files
CSV_DIR = "daily_predictions"
os.makedirs(CSV_DIR, exist_ok=True)  # Create directory if it doesn't exist

# Directory to save data files (e.g., consumption, weather)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)  # Create directory if it doesn't exist

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log incoming request data
        app.logger.info("Received request data: %s", request.json)

        # Extract forecast_hours from request body
        forecast_hours = request.json.get('forecast_hours', 24)
        app.logger.info("Forecast hours: %d", forecast_hours)

        # Get predictions from the model
        predictions = model.predict(forecast_hours)
        app.logger.info("Raw predictions: %s", predictions)

        # Format predictions into a list of dictionaries
        formatted_predictions = [
            {
                "date": p["ds"].strftime("%d-%m-%Y"),  # Format date as string
                "hour": p["ds"].hour,                 # Extract hour from datetime
                "generation": p["yhat"]              # Use yhat as generation
            }
            for p in predictions
        ]
        app.logger.info("Formatted predictions: %s", formatted_predictions)

        # Save predictions to a CSV file
        csv_filename = os.path.join(CSV_DIR, f"predictions_{formatted_predictions[0]['date']}.csv")
        with open(csv_filename, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["date", "hour", "generation"])
            writer.writeheader()  # Write column headers
            writer.writerows(formatted_predictions)  # Write prediction rows
        app.logger.info("Predictions saved to: %s", csv_filename)

        # Return predictions as JSON response
        return jsonify({"message": "Predictions fetched successfully", "predictions": formatted_predictions}), 200

    except Exception as e:
        app.logger.error("Error in /predict: %s", str(e))
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


@app.route('/consumption/current', methods=['GET'])
def get_current_consumption():
    try:
        # Current date and hour
        now = datetime.now()
        current_date = now.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
        current_hour = now.hour  # Get current hour

        # Path to the consumption file
        csv_path = os.path.join(DATA_DIR, "consumption_data.csv")

        # Check if the file exists
        if not os.path.exists(csv_path):
            return jsonify({"error": "Consumption file not found"}), 404

        # Load consumption data using pandas
        data = pd.read_csv(csv_path)

        # Log the current date and hour for debugging
        app.logger.info(f"Current Date: {current_date}, Current Hour: {current_hour}")

        # Assuming the 'hour' column has time in 'hh:mm:ss' format, 
        # we need to extract the hour part from the time string.
        data['hour'] = data['hour'].apply(lambda x: int(x.split(':')[0]))  # Extract the hour from 'hh:mm:ss'

        # Log the first few rows of data to ensure it's loaded correctly
        app.logger.info(f"Data Preview:\n{data.head()}")

        # Filter data for current date and hour
        filtered_data = data[
            (data['date'] == current_date) & 
            (data['hour'] == current_hour)
        ]

        # Log the filtered data to check if it matches the current time
        app.logger.info(f"Filtered Data:\n{filtered_data}")

        # If no data is found, return an empty response
        if filtered_data.empty:
            return jsonify({"message": "No data found for the current time"}), 200

        # Convert the first matching row to a dictionary
        result = filtered_data.iloc[0].to_dict()

        return jsonify({
            "message": "Consumption data fetched successfully",
            "data": result
        }), 200

    except Exception as e:
        app.logger.error("Error in /consumption/current: %s", str(e))
        return jsonify({"error": f"Error fetching consumption data: {str(e)}"}), 500


# New endpoint to fetch all consumption data (CSV)
@app.route('/consumption', methods=['GET'])
def get_consumption():
    try:
        # Get today's date in dd-mm-yyyy format
        today_date = datetime.now().strftime('%d-%m-%Y')

        # Path to the consumption file
        csv_path = os.path.join(DATA_DIR, "consumption_data.csv")

        # Check if the file exists
        if not os.path.exists(csv_path):
            return jsonify({"error": "Consumption file not found"}), 404

        # Load consumption data using pandas
        data = pd.read_csv(csv_path)

        # Ensure the 'date' column is in datetime format with the correct format (dd-mm-yyyy)
        data['date'] = pd.to_datetime(data['date'], format='%d-%m-%Y').dt.date

        # Filter data for today's date
        today_data = data[data['date'] == datetime.now().date()]

        # Check if there is any consumption data for today
        if today_data.empty:
            return jsonify({"message": "No consumption data found for today"}), 200

        # Format the response to return data for the last 24 hours
        result = today_data.to_dict(orient='records')

        return jsonify({
            "message": "Consumption data for today",
            "data": result
        }), 200

    except Exception as e:
        app.logger.error("Error in /consumption: %s", str(e))
        return jsonify({"error": f"Error fetching consumption data: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
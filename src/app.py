"""
Flask APP
"""

import os

import pandas as pd
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from loguru import logger

from src.inference import load_model, predict

load_dotenv()

app = Flask(__name__)

logger.info("Starting the app")
logger.info("Loading the model")
MODELS_PATH = os.getenv("MODEL_PATH")
MODEL_PATH = os.path.join(MODELS_PATH, "model.joblib")
MODEL = load_model(MODEL_PATH)
logger.info("Model loaded successfully")

CLASSES = ["Setosa", "Versicolor", "Virginica"]

@app.route("/", methods=["GET"])
def healthcheck():
    """
    Main endpoint for healthcheckS
    """
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def prediction_func():
    """
    Endpoint for prediction
    """

    logger.info("Predictions started")
    try:
        data = request.get_json()
        logger.info("Data received")
        df = pd.DataFrame(data, index=[0])
        logger.info("Dataframe created")
        prediction = predict(MODEL, df)
        logger.info("Prediction made")
        postprocessed_preds = CLASSES[prediction[0]]
        logger.info("Prediction postprocessed")
        return jsonify({"prediction": postprocessed_preds})
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 555

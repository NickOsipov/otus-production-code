"""
Module: inference.py
"""

import joblib
import pandas as pd
from sklearn.base import BaseEstimator


def load_model(model_path: str) -> object:
    """
    Load a model from a file
    """
    return joblib.load(model_path)


def predict(model: BaseEstimator, data: pd.DataFrame) -> object:
    """
    Make a prediction using a trained model
    """
    return model.predict(data)

import joblib
from tensorflow import keras


def load_recommendation_model(model_path):
    return keras.models.load_model(model_path)


def load_similar_model(model_path):
    return joblib.load(model_path)

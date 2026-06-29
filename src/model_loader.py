import joblib

from utils.constants import MODEL_PATH
from utils.constants import ENCODER_PATH

def load_model():
    model = joblib.load(MODEL_PATH)
    return model

def load_encoders():
    encoders = joblib.load(ENCODER_PATH)
    return encoders
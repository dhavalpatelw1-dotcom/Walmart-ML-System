import pickle
import os
BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.abspath(
    os.path.join(BASE_DIR, "../../model/walmart_best_model.pkl")
)

model = pickle.load(open(MODEL_PATH, "rb"))


def get_model():
    return model
import joblib
import numpy as np
from sklearn import svm

from .interfaces import ModelInterface


class IrisModel(ModelInterface):
    def __init__(self) -> None:
        self.model = svm.SVC()

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        self.model.fit(X, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.model.predict(X)

    def save(self, path: str) -> None:
        joblib.dump(self.model, path)

    def load(self, path: str) -> None:
        self.model = joblib.load(path)

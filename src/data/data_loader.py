import numpy as np
from sklearn import datasets


class DataLoader:
    @staticmethod
    def load_iris_data() -> tuple[np.ndarray, np.ndarray]:
        iris = datasets.load_iris()
        return iris.data, iris.target

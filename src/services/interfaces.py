from abc import ABC, abstractmethod

import numpy as np


class ClassifierServiceInterface(ABC):
    @abstractmethod
    def classify(self, input_data: np.ndarray) -> np.ndarray: ...

from typing import Annotated

import numpy as np
from bentoml.validators import Shape
from pydantic import Field

import bentoml
from config.config import Config
from models.interfaces import ModelInterface
from models.model_factory import ModelFactory

from .interfaces import ClassifierServiceInterface

DEFAULT_INPUT: np.ndarray = np.array([[5.2, 2.3, 5.0, 0.7]])


def load_default_model() -> ModelInterface:
    bento_model = bentoml.models.get(
        f"{Config.MODEL_TYPE}_sklearn:{Config.MODEL_VERSION}"
    )
    model = ModelFactory.create_model(Config.MODEL_TYPE)
    model.load(bento_model.path_of("model.pkl"))
    return model


class IrisClassifier(ClassifierServiceInterface):
    """Plain, framework-free classifier used both by the API layer and by tests."""

    def __init__(self, model: ModelInterface | None = None) -> None:
        self.model = model or load_default_model()

    def classify(self, input_data: np.ndarray) -> np.ndarray:
        return self.model.predict(input_data)


@bentoml.service(
    resources={
        "cpu": "1",
        "memory": "2Gi",
    },
)
class IrisClassifierService:
    def __init__(self) -> None:
        self._classifier = IrisClassifier()

    @bentoml.api
    def classify(
        self,
        input_series: Annotated[np.ndarray, Shape((-1, 4))] = Field(
            default=DEFAULT_INPUT
        ),
    ) -> np.ndarray:
        return self._classifier.classify(input_series)

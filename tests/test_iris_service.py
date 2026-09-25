import numpy as np

from data.data_loader import DataLoader
from models.iris_model import IrisModel
from services.iris_service import IrisClassifier


def _trained_model() -> IrisModel:
    X, y = DataLoader.load_iris_data()
    model = IrisModel()
    model.train(X, y)
    return model


def test_classify_uses_injected_model() -> None:
    classifier = IrisClassifier(model=_trained_model())

    result = classifier.classify(np.array([[5.2, 2.3, 5.0, 0.7]]))

    assert result.shape == (1,)
    assert result[0] in {0, 1, 2}

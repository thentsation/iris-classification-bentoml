import numpy as np

from data.data_loader import DataLoader
from models.iris_model import IrisModel


def test_train_and_predict_returns_known_labels() -> None:
    X, y = DataLoader.load_iris_data()
    model = IrisModel()
    model.train(X, y)

    predictions = model.predict(X[:5])

    assert predictions.shape == (5,)
    assert set(predictions.tolist()).issubset({0, 1, 2})


def test_save_and_load_roundtrip(tmp_path) -> None:
    X, y = DataLoader.load_iris_data()
    model = IrisModel()
    model.train(X, y)

    model_path = tmp_path / "model.pkl"
    model.save(str(model_path))

    loaded = IrisModel()
    loaded.load(str(model_path))

    np.testing.assert_array_equal(loaded.predict(X), model.predict(X))

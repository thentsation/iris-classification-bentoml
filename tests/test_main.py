from data.data_loader import DataLoader
from main import train_and_save_model
from models.iris_model import IrisModel


def test_train_and_save_model_roundtrip() -> None:
    bento_model = train_and_save_model()

    loaded = IrisModel()
    loaded.load(bento_model.path_of("model.pkl"))

    X, _ = DataLoader.load_iris_data()
    predictions = loaded.predict(X[:3])
    assert predictions.shape == (3,)

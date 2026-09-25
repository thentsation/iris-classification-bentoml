import bentoml
from config.config import Config
from data.data_loader import DataLoader
from data.data_preprocessor import DataPreprocessor
from models.model_factory import ModelFactory


def train_and_save_model() -> bentoml.Model:
    model = ModelFactory.create_model(Config.MODEL_TYPE)

    X, y = DataLoader.load_iris_data()
    X = DataPreprocessor.preprocess_input(X)

    model.train(X, y)

    with bentoml.models.create(f"{Config.MODEL_TYPE}_sklearn") as bento_model:
        model.save(bento_model.path_of("model.pkl"))
    return bento_model


if __name__ == "__main__":
    saved_model = train_and_save_model()
    print(f"Model saved: {saved_model}")

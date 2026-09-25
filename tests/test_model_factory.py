import pytest

from models.iris_model import IrisModel
from models.model_factory import ModelFactory


def test_creates_iris_model_case_insensitive() -> None:
    assert isinstance(ModelFactory.create_model("iris"), IrisModel)
    assert isinstance(ModelFactory.create_model("IRIS"), IrisModel)


def test_unknown_model_type_raises() -> None:
    with pytest.raises(ValueError, match="Unknown model type"):
        ModelFactory.create_model("unknown")

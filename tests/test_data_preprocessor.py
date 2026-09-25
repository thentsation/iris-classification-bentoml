import numpy as np

from data.data_preprocessor import DataPreprocessor


def test_preprocess_input_is_identity() -> None:
    data = np.array([[1.0, 2.0, 3.0, 4.0]])
    result = DataPreprocessor.preprocess_input(data)
    assert np.array_equal(result, data)

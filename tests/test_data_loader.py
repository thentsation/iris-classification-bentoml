from data.data_loader import DataLoader


def test_load_iris_data_shapes_and_classes() -> None:
    X, y = DataLoader.load_iris_data()

    assert X.shape == (150, 4)
    assert y.shape == (150,)
    assert set(y.tolist()) == {0, 1, 2}

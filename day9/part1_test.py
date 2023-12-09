import numpy as np
from part1 import get_prediction


def test_get_prediction():
    """Test get_prediction() function."""
    assert get_prediction(np.array([0, 3, 6, 9, 12, 15])) == 18
    assert get_prediction(np.array([1, 3, 6, 10, 15, 21])) == 28
    assert get_prediction(np.array([10, 13, 16, 21, 30, 45])) == 68

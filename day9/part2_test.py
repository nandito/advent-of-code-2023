from part2 import rolling_diff


def test_rolling_diff():
    """Test rolling_diff() function."""
    assert rolling_diff([2, 0, 3, 10]) == [0, 2, -2, 5]

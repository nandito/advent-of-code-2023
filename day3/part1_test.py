from part1 import has_adjacent_symbol

sample_matrix = [
    ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
    [".", ".", ".", "*", ".", ".", ".", ".", ".", "."],
    [".", ".", "3", "5", ".", ".", "6", "3", "3", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
    ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "+", ".", "5", "8", "."],
    [".", ".", "5", "9", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "7", "5", "5", "."],
    [".", ".", ".", "$", ".", "*", ".", ".", ".", "."],
    [".", "6", "6", "4", ".", "5", "9", "8", ".", "."],
]


def test_has_adjacent_sympbol():
    """Test has_adjacent_sympbol"""
    assert has_adjacent_symbol(0, 0, sample_matrix) is False
    assert has_adjacent_symbol(0, 1, sample_matrix) is False
    assert has_adjacent_symbol(0, 2, sample_matrix) is True
    assert has_adjacent_symbol(0, 5, sample_matrix) is False
    assert has_adjacent_symbol(0, 6, sample_matrix) is False
    assert has_adjacent_symbol(0, 7, sample_matrix) is False

    assert has_adjacent_symbol(2, 2, sample_matrix) is True
    assert has_adjacent_symbol(2, 3, sample_matrix) is True

    assert has_adjacent_symbol(9, 1, sample_matrix) is False
    assert has_adjacent_symbol(9, 2, sample_matrix) is True
    assert has_adjacent_symbol(9, 3, sample_matrix) is True

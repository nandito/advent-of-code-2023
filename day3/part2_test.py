import numpy as np

from part2 import (
    find_gear_char_positions,
    get_surrounding_numbers,
    get_full_digit,
    filter_same_numbers,
)

sample_matrix = np.array(
    [
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
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "6", "6", "4", "*", "5", "9", "8", ".", "."],
    ]
)


def test_find_gear_char_positions():
    """Test find_gear_char_positions function."""
    # assert (
    #     find_gear_char_positions(sample_matrix) == np.array([[1, 3], [4, 3], [8, 5]])
    # ).all()
    assert (
        find_gear_char_positions(sample_matrix) == np.array([[1, 3], [4, 3], [8, 5], [11,4]])
    ).all()


def test_get_full_digit():
    """Test get_full_digit function."""
    assert get_full_digit("5", [2, 3], sample_matrix) == 35
    assert get_full_digit("7", [0, 2], sample_matrix) == 467
    assert get_full_digit("3", [2, 2], sample_matrix) == 35


def test_filter_same_numbers():
    """Test filter_same_numbers"""
    assert filter_same_numbers([["5", [2, 3]], ["7", [0, 2]], ["3", [2, 2]]]) == [
        ["5", [2, 3]],
        ["7", [0, 2]],
    ]


def test_get_surrounding_numbers():
    """Test get_surrounding_numbers function."""
    assert get_surrounding_numbers([1, 3], sample_matrix) == [35, 467]
    assert get_surrounding_numbers([4, 3], sample_matrix) == [617]
    assert get_surrounding_numbers([8, 5], sample_matrix) == [598, 755]
    assert get_surrounding_numbers([11, 4], sample_matrix) == [664, 598]

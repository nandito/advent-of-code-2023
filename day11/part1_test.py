import numpy as np

from part1 import expand_space


def test_expand_space():
    """Test expand_space()"""
    assert expand_space(
        np.array(
            [
                [".", ".", "#"],
                [".", ".", "."],
                [".", "#", "."],
            ]
        ),
        expand_by=1,
    ) == [
        [".", ".", ".", "#"],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", "#", "."],
    ]
    assert expand_space(
        np.array(
            [
                [".", ".", "#"],
                [".", ".", "."],
                [".", "#", "."],
            ]
        ),
        expand_by=2,
    ) == [
        [".", ".", ".", ".", "#"],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", "#", "."],
    ]

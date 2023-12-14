from part1 import tilt

# Input:
"""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

# Expected output:
"""
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""


def test_tilt():
    """Test the tilt function."""
    assert tilt(["O", "O", ".", "O", ".", "O", ".", ".", "#", "#"]) == [
        "O",
        "O",
        "O",
        "O",
        ".",
        ".",
        ".",
        ".",
        "#",
        "#",
    ]
    assert tilt(["O", "O", ".", "O", ".", "O", ".", ".", "#", "O"]) == [
        "O",
        "O",
        "O",
        "O",
        ".",
        ".",
        ".",
        ".",
        "#",
        "O",
    ]
    assert tilt([".", "O", ".", ".", ".", "#", "O", ".", ".", "O"]) == [
        "O",
        ".",
        ".",
        ".",
        ".",
        "#",
        "O",
        "O",
        ".",
        ".",
    ]
    assert tilt(["#", ".", "#", ".", ".", "O", "#", ".", "#", "#"]) == [
        "#",
        ".",
        "#",
        "O",
        ".",
        ".",
        "#",
        ".",
        "#",
        "#",
    ]

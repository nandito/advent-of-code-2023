from part2 import get_max_cube_counts_product


def test_get_max_cube_counts_product():
    """Test get_max_cube_counts_product function."""
    assert (
        get_max_cube_counts_product(
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        )
        == 48
    )

    assert (
        get_max_cube_counts_product(
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        )
        == 12
    )
    assert (
        get_max_cube_counts_product(
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        )
        == 1560
    )
    assert (
        get_max_cube_counts_product(
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        == 630
    )
    assert (
        get_max_cube_counts_product(
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        )
        == 36
    )

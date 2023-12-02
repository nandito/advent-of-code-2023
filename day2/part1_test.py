from part1 import check_possibility


def test_check_possibility():
    """Test check_possibility function."""
    assert check_possibility(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    ) == ("1", True)
    assert check_possibility(
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
    ) == ("2", True)
    assert check_possibility(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    ) == ("3", False)
    assert check_possibility(
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
    ) == ("4", False)
    assert check_possibility(
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
    ) == ("5", True)

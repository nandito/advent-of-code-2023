from part1 import DIRECTIONS, get_directions


def test_get_directions():
    """Test get_directions function"""
    assert get_directions(".", DIRECTIONS["up"]) == [DIRECTIONS["up"]]
    assert get_directions(".", DIRECTIONS["down"]) == [DIRECTIONS["down"]]
    assert get_directions(".", DIRECTIONS["left"]) == [DIRECTIONS["left"]]
    assert get_directions(".", DIRECTIONS["right"]) == [DIRECTIONS["right"]]
    assert get_directions("\\", DIRECTIONS["up"]) == [DIRECTIONS["left"]]
    assert get_directions("\\", DIRECTIONS["down"]) == [DIRECTIONS["right"]]
    assert get_directions("\\", DIRECTIONS["left"]) == [DIRECTIONS["up"]]
    assert get_directions("\\", DIRECTIONS["right"]) == [DIRECTIONS["down"]]
    assert get_directions("/", DIRECTIONS["up"]) == [DIRECTIONS["right"]]
    assert get_directions("/", DIRECTIONS["down"]) == [DIRECTIONS["left"]]
    assert get_directions("/", DIRECTIONS["left"]) == [DIRECTIONS["down"]]
    assert get_directions("/", DIRECTIONS["right"]) == [DIRECTIONS["up"]]
    assert get_directions("|", DIRECTIONS["up"]) == [DIRECTIONS["up"]]
    assert get_directions("|", DIRECTIONS["down"]) == [DIRECTIONS["down"]]
    assert get_directions("|", DIRECTIONS["left"]) == [
        DIRECTIONS["up"],
        DIRECTIONS["down"],
    ]
    assert get_directions("|", DIRECTIONS["right"]) == [
        DIRECTIONS["up"],
        DIRECTIONS["down"],
    ]
    assert get_directions("-", DIRECTIONS["left"]) == [DIRECTIONS["left"]]
    assert get_directions("-", DIRECTIONS["right"]) == [DIRECTIONS["right"]]
    assert get_directions("-", DIRECTIONS["up"]) == [
        DIRECTIONS["left"],
        DIRECTIONS["right"],
    ]
    assert get_directions("-", DIRECTIONS["down"]) == [
        DIRECTIONS["left"],
        DIRECTIONS["right"],
    ]

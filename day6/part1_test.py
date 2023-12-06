from part1 import parse_input, get_possible_distances


def test_parse_input():
    input = ["Time: 1 2 3 4 5", "Distance: 5 4 3 2 1"]
    [time, distance] = parse_input(input)
    assert time == [1, 2, 3, 4, 5]
    assert distance == [5, 4, 3, 2, 1]


def test_get_possible_distances():
    distances = get_possible_distances(7)
    assert distances == [6, 10, 12, 12, 10, 6]

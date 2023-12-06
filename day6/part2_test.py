from part2 import parse_input 


def test_parse_input():
    input = ["Time: 1 2 3 4 5", "Distance: 5 4 3 2 1"]
    [time, distance] = parse_input(input)
    assert time == 12345
    assert distance == 54321



from part1 import process_mappings


def test_process_mappings():
    """Test process_mappings function"""
    # seed to soil
    assert process_mappings([[50, 98, 2], [52, 50, 48]], [79, 14, 55, 13]) == [
        81,
        14,
        57,
        13,
    ]

    # soil-to-fertilizer
    assert process_mappings(
        [[0, 15, 37], [37, 52, 2], [39, 0, 15]], [81, 14, 57, 13]
    ) == [81, 53, 57, 52]

    # fertilizer-to-water
    assert process_mappings(
        [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], [81, 53, 57, 52]
    ) == [81, 49, 53, 41]

    # water-to-light
    assert process_mappings([[88, 18, 7], [18, 25, 70]], [81, 49, 53, 41]) == [
        74,
        42,
        46,
        34,
    ]

    # light-to-temperature
    assert process_mappings(
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [74, 42, 46, 34],
    ) == [78, 42, 82, 34]

    # temperature-to-humidity
    assert process_mappings(
        [[0, 69, 1], [1, 0, 69]],
        [78, 42, 82, 34],
    ) == [78, 43, 82, 35]

    # humidity-to-location
    assert process_mappings(
        [[60, 56, 37], [56, 93, 4]],
        [78, 43, 82, 35],
    ) == [82, 43, 86, 35]

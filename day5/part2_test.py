from part2 import get_subrange_left, get_subrange_right, process_mappings


def test_process_mappings():
    """Test process_mappings function"""
    # seed to soil
    # numbers_to_match [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    # assert process_mappings([[50, 98, 2], [52, 50, 48]], [79, 14, 55, 13]) == [
    #     81,
    #     14,
    #     57,
    #     13,
    # ]

    # # soil to fertilizer
    # # numbers_to_match [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    # assert process_mappings(
    #     [[0, 15, 37], [37, 52, 2], [39, 0, 15]], [81, 14, 57, 13]
    # ) == [81, 14, 57, 13]

    # # fertilizer to water
    # # numbers_to_match [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 53, 54, 55, 56, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    # assert process_mappings(
    #     [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], [81, 14, 57, 13]
    # ) == [81, 14, 53, 4, 61, 9]

    # # water to light
    # # numbers_to_match [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 46, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62]
    # assert process_mappings([[88, 18, 7], [18, 25, 70]], [81, 14, 53, 4, 61, 9]) == [
    #     74,
    #     14,
    #     46,
    #     4,
    #     54,
    #     9,
    # ]

    # light to temperature
    # numbers_to_match [78, 79, 80, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 96, 97, 98]
    assert process_mappings(
        [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
        [74, 14, 46, 4, 54, 9],
    ) == [78, 3, 45, 11, 82, 4, 90, 9]


# map_title ('temperature', 'humidity')
# numbers_to_match [78, 79, 80, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 82, 83, 84, 85, 90, 91, 92, 93, 94, 95, 96, 97, 98]
# map_title ('humidity', 'location')

# assert process_mappings()


# def test_get_subrange_left():
#     """Test get_subrange_left function"""
#     assert get_subrange_left([57, 70], [53, 61]) == [[53, 4], [61, 9]]

# def test_get_subrange_right():
#     """Test get_subrange_right function"""
#     assert get_subrange_right([74,88], [77,100]) == [[78, 3]]
#     # assert get_subrange_right([74,88], [77,100]) == [[78, 3], [45, 11]]

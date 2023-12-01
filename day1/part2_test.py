from part2 import (
    find_all,
    get_larger_num,
    get_numbers,
    get_number_words,
    find_smallest_index,
    find_largest_index,
    get_smaller_num,
    get_string_and_digit_numbers,
)


def test_find_all():
    """Test find_all function."""
    assert list(find_all("two1nine", "two")) == [0]
    assert list(find_all("two1nine", "nine")) == [4]
    assert list(find_all("eightwothree", "eight")) == [0]
    assert list(find_all("eightwothree", "two")) == [4]
    assert list(find_all("eightwothree", "three")) == [7]
    assert list(find_all("eightwothree", "one")) == []
    assert list(find_all("4nineeightseven2", "nine")) == [1]
    assert list(find_all("7pqrstsixteensixsix", "six")) == [6, 13, 16]


def test_get_numbers():
    """Test get_numbers function."""
    assert get_numbers("two1nine") == {"1": [3]}
    assert get_numbers("eightwothree") == {}
    assert get_numbers("abcone2threexyz") == {"2": [6]}
    assert get_numbers("xtwone3four") == {"3": [6]}
    assert get_numbers("4nineeightseven2") == {"4": [0], "2": [15]}
    assert get_numbers("zoneight234") == {"2": [8], "3": [9], "4": [10]}
    assert get_numbers("7pqrstsixteen") == {"7": [0]}
    assert get_numbers("7pqrst7sixteen7") == {"7": [0, 6, 14]}


def test_get_number_words():
    """Test get_number_words function."""
    assert get_number_words("two1nine") == {"2": [0], "9": [4]}
    assert get_number_words("eightwothree") == {"8": [0], "2": [4], "3": [7]}
    assert get_number_words("abcone2threexyz") == {"1": [3], "3": [7]}
    assert get_number_words("xtwone3four") == {"2": [1], "1": [3], "4": [7]}
    assert get_number_words("4nineeightseven2") == {"9": [1], "8": [5], "7": [10]}
    assert get_number_words("zoneight234") == {"1": [1], "8": [3]}
    assert get_number_words("7pqrstsixteen") == {"6": [6]}
    assert get_number_words("7pqrst7sixteen7sixsix") == {"6": [7, 15, 18]}


def test_find_smallest_index():
    """Test find_smallest_index function."""
    assert find_smallest_index({"2": [0], "9": [4]}) == ["2", 0]
    assert find_smallest_index({"8": [0], "2": [4], "3": [7]}) == ["8", 0]
    assert find_smallest_index({"1": [3], "3": [7]}) == ["1", 3]
    assert find_smallest_index({"2": [1], "1": [3], "4": [7]}) == ["2", 1]
    assert find_smallest_index({"9": [1], "8": [5], "7": [10]}) == ["9", 1]
    assert find_smallest_index({"1": [1], "8": [3]}) == ["1", 1]
    assert find_smallest_index({"6": [6]}) == ["6", 6]
    assert find_smallest_index({"6": [7, 15, 18]}) == ["6", 7]


def test_find_largest_index():
    """Test find_largest_index function."""
    assert find_largest_index({"2": [0], "9": [4]}) == ["9", 4]
    assert find_largest_index({"8": [0], "2": [4], "3": [7]}) == ["3", 7]
    assert find_largest_index({"1": [3], "3": [7]}) == ["3", 7]
    assert find_largest_index({"2": [1], "1": [3], "4": [7]}) == ["4", 7]
    assert find_largest_index({"9": [1], "8": [5], "7": [10]}) == ["7", 10]
    assert find_largest_index({"1": [1], "8": [3]}) == ["8", 3]
    assert find_largest_index({"6": [6]}) == ["6", 6]
    assert find_largest_index({"6": [7, 15, 18]}) == ["6", 18]


def test_get_smaller_num():
    """Test get_smaller_num function."""
    assert get_smaller_num(["2", 0], ["9", 4]) == "2"
    assert get_smaller_num(["9", 1], ["7", 10]) == "9"
    assert get_smaller_num(["7", 10], ["9", 1]) == "9"
    assert get_smaller_num(["8", 3], ["1", 1]) == "1"
    assert get_smaller_num([], ["9", 4]) == "9"
    assert get_smaller_num(["9", 4], []) == "9"


def test_get_larger_num():
    """Test get_larger_num function."""
    assert get_larger_num(["2", 0], ["9", 4]) == "9"
    assert get_larger_num(["9", 1], ["7", 10]) == "7"
    assert get_larger_num(["7", 10], ["9", 1]) == "7"
    assert get_larger_num(["8", 3], ["1", 1]) == "8"
    assert get_larger_num([], ["9", 4]) == "9"
    assert get_larger_num(["9", 4], []) == "9"


def test_get_string_and_digit_numbers():
    """Test get_string_and_digit_numbers function."""
    assert get_string_and_digit_numbers("two1nine") == 29
    assert get_string_and_digit_numbers("eightwothree") == 83
    assert get_string_and_digit_numbers("abcone2threexyz") == 13
    assert get_string_and_digit_numbers("xtwone3four") == 24
    assert get_string_and_digit_numbers("4nineeightseven2") == 42
    assert get_string_and_digit_numbers("zoneight234") == 14
    assert get_string_and_digit_numbers("7pqrstsixteen") == 76

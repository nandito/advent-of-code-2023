"""Number words in order from one to nine."""
number_word_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

NumberIndicesDict = dict[str, list[int]]


def find_all(a_str: str, sub: str):
    """
    Find all occurrences of a substring in a string.
    :param a_str: string to search in
    :param sub: substring to search for
    :return: generator of all occurrences
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def get_numbers(line: str) -> NumberIndicesDict:
    """
    Get the digits and their index in a string.
    :param line: string to search in
    :return: dictionary of digits and their indices in an array
    """
    matches = {}
    chars = [*line]
    for idx, char in enumerate(chars):
        if char.isdigit():
            matches[char] = [*matches[char], idx] if char in matches else [idx]
    return matches


def get_number_words(line) -> NumberIndicesDict:
    """
    Get the number words and their index in a string.
    :param line: string to search in
    :return: dictionary of number words and their indices in an array
    """
    matches = {}
    for idx, word in enumerate(number_word_list):
        word_matches = list(find_all(line, word))
        if len(word_matches):
            num = idx + 1
            matches[str(num)] = word_matches

    return matches


def find_smallest_index(dictionary: NumberIndicesDict):
    """
    Find the smallest index in a dictionary of "number": [indices].
    :param dictionary: dictionary of "number": [indices]
    :return: ["number", index]
    """
    smallest_idx = 100000
    number_with_index = []
    for k, v in dictionary.items():
        for match in v:
            if match < smallest_idx:
                smallest_idx = match
                number_with_index = [str(k), match]
    return number_with_index


def find_largest_index(dictionary):
    """
    Find the largest index in a dictionary of "number": [indices].
    :param dictionary: dictionary of "number": [indices]
    :return: ["number", index]
    """
    largest_idx = -1
    number_with_index = []
    for k, v in dictionary.items():
        for match in v:
            if match > largest_idx:
                largest_idx = match
                number_with_index = [str(k), match]
    return number_with_index


def get_smaller_num(d1, d2):
    """
    Compare two arrays by their second element and return the smaller ones first element.
    :param d1: array of [number, index]
    :param d2: array of [number, index]
    :return: smaller number
    """
    if len(d1) == 0:
        return d2[0]
    if len(d2) == 0:
        return d1[0]
    return d1[0] if d1[1] < d2[1] else d2[0]


def get_larger_num(d1, d2):
    """
    Compare two arrays by their second element and return the larger ones first element.
    :param d1: array of [number, index]
    :param d2: array of [number, index]
    :return: larger number
    """
    if len(d1) == 0:
        return d2[0]
    if len(d2) == 0:
        return d1[0]
    return d1[0] if d1[1] > d2[1] else d2[0]


def get_string_and_digit_numbers(line):
    """
    Get the smallest and largest digit in a string.
    :param line: string to search in
    :return: smallest and largest digit
    """
    numbers = get_numbers(line)
    number_words = get_number_words(line)
    smallest_number_word = find_smallest_index(number_words)
    smallest_number = find_smallest_index(numbers)
    smallest_digit = get_smaller_num(smallest_number, smallest_number_word)

    largest_number_word = find_largest_index(number_words)
    largest_number = find_largest_index(numbers)
    largest_digit = get_larger_num(largest_number, largest_number_word)
    # print(line, smallest_digit+largest_digit)
    # print("numbers:",numbers,"number_words:", number_words)
    # print("smallest_num_w:",smallest_number_word, "smallest_num:", smallest_number, "largest_num_w:",largest_number_word, "largest_num:",largest_number)
    return int(smallest_digit + largest_digit)


with open("input") as f:
    row_values = []
    for file_line in f:
        row_value = get_string_and_digit_numbers(file_line)
        row_values.append(row_value)
    sums = sum(row_values)
    print(sums)

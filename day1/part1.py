from io import TextIOWrapper


def get_numbers(line: str):
    """
    Get the sum of the first and last digit of a string of numbers.
    :param line: string of numbers
    :return: concatenation of the first and last digit
    """

    chars = [*line]
    first_digit = None
    cache_digit = None
    for char in chars:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            else:
                cache_digit = char

    last_digit = cache_digit if cache_digit is not None else first_digit

    return first_digit + last_digit


def solve_part1(file: TextIOWrapper):
    """
    Solve part 1 of the puzzle.
    :param file: opened file 
    :return: None
    """
    row_values = []
    for file_line in file:
        row_value = get_numbers(file_line)
        row_values.append(row_value)
    sums = sum([int(n) for n in row_values])
    print(sums)

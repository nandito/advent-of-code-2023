def get_numbers(line):
    chars = [*line]
    first_digit = None
    cache_digit = None
    for c in chars:
        if c.isdigit():
            if first_digit is None:
                first_digit = c
            else:
                cache_digit = c

    last_digit = cache_digit if cache_digit is not None else first_digit

    return first_digit + last_digit


with open('input') as f:
    row_values = []
    for line in f:
        row_value = get_numbers(line)
        row_values.append(row_value)
    sums = sum([int(n) for n in row_values])
    print(sums)

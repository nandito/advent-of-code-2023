import numpy as np

# 1. find gear char positions
# 2. look around the gear char:
#       if any char around is a number: add to gear_numbers=[]
#       return gear_numbers[]
# 3. push the multiplication of the gear_numbers to a gear=[] if it has length 2
# 4. sum up gear


def find_gear_char_positions(matrix):
    elements = np.where(matrix == "*")
    indices = np.asarray(elements).T
    return indices


def get_full_digit(digit, position, matrix):
    # decrease the 2nd num until 0th col | non-numeric => insert numeric before
    # increate the 2nd num until end of col | non-numeric => append numeric after
    # print(digit)
    full_digit = digit
    range_before = range(0, position[1])
    range_after = range(position[1] + 1, len(matrix[0]))
    # Check chars before - [::-1] reverses the range
    for col in range_before[::-1]:
        ch = matrix[position[0]][col]
        if ch.isnumeric():
            full_digit = ch + full_digit
        else:
            break

    for col in range_after:
        ch = matrix[position[0]][col]
        if ch.isnumeric():
            full_digit = full_digit + ch
        else:
            break

    return int(full_digit)


def filter_same_numbers(surrounding_digits):
    # cords = [n[1] for n in surrounding_digits]
    uniques = []
    row_cache = {}
    # for cord in cords:

    for sd in surrounding_digits:
        # print("digit_cords", sd[1])
        row = sd[1][0]
        col = sd[1][1]
        if row in row_cache:
            row_cache[row] = [*row_cache[row], col]
            # if already in the row but col row diff is > 1 => unique
            issame = (col + 1) in row_cache[row] or (col - 1) in row_cache[row]
            if not issame:
                uniques.append(sd)

        else:
            row_cache[row] = [col]
            uniques.append(sd)

        # print("row_cache:", row_cache)
    # print("uniques: ", uniques)
    return uniques


surrounding_positions = [
    [-1, 0],  # left
    [1, 0],  # right
    [-1, -1],  # top left
    [0, -1],  # top center
    [1, -1],  # top right
    [-1, 1],  # bottom left
    [0, 1],  # bottom center
    [1, 1],  # bottom right
]


def get_surrounding_numbers(position, matrix):
    # print(matrix)
    surrounding_digits = []
    for surrounding_pos in surrounding_positions:
        row = surrounding_pos[0] + position[0]
        col = surrounding_pos[1] + position[1]
        if row < 0:
            continue
        if col < 0:
            continue

        try:
            char = matrix[row][col]
            # print(row, col, char)
            if char.isnumeric():
                surrounding_digits.append([char, [row, col]])
        except IndexError:
            # print("index error for:", direction)
            pass
    filtered = filter_same_numbers(surrounding_digits)
    nums = [get_full_digit(digit, pos, matrix) for [digit, pos] in filtered]
    # print(nums)
    return nums

    # filter overlaps, when rows equals and col has 1 diff


with open("input") as f:
    m = np.array([])
    for file_line in f:
        m = np.array([*m, [*file_line.strip()]])

    gear_chars = find_gear_char_positions(m)
    surrounding_numbers = [get_surrounding_numbers(pos, m) for pos in gear_chars]
    gears = []
    for sn in surrounding_numbers:
        if len(sn) == 2:
            gears.append(np.prod(sn))
    print(sum(gears))

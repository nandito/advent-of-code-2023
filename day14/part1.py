import numpy as np


def tilt(row):
    new_row = []
    block = 0
    for i in range(len(row)):
        if row[i] == "O":
            new_row.insert(block, "O")
        elif row[i] == "#":
            block = i + 1
            new_row.append("#")
        else:
            new_row.append(row[i])
    return new_row


def sum_up(rows):
    counts = np.array(
        list(map(lambda row: np.count_nonzero(np.array(row) == "O"), rows))
    )
    reversed_counts = np.flip(counts)
    # print(counts)
    # print(reversed_counts)
    total = sum(
        list(map(lambda idx: (idx + 1) * reversed_counts[idx], range(len(counts))))
    )
    return total


def solve_part1(lines):
    rows = np.array([[*line.strip()] for line in lines])
    tilted_rows = np.array(list(map(tilt, rows.T))).T
    # print(tilted_rows)
    total = sum_up(tilted_rows)
    return total


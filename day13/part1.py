import numpy as np


def validate_pairs(pairs, part):
    matchings = []
    real_matches = []
    for pair in pairs:
        # print("validating pair", pair)
        real_match = True
        for idx, col in enumerate(part):
            pairs_to_check = [pair[0] + idx, pair[1] - idx]
            if pairs_to_check[0] > len(col) or pairs_to_check[1] < 0:
                break
            try:
                if np.array_equal(
                    part[:, pairs_to_check[0]], part[:, pairs_to_check[1]]
                ):
                    # print("matching", pairs_to_check)
                    matchings.append(pairs_to_check)
                else:
                    # print("not matching", pairs_to_check)
                    real_match = False
            except IndexError:
                continue
        real_matches.append(real_match)
    return real_matches


def parse_map(lines):
    my_map = []
    partial_map = []
    for line in lines:
        if line == "\n":
            my_map.append(np.array([*map(list, partial_map)]))
            partial_map = []

        else:
            partial_map.append(line.strip())

    my_map.append(np.array([*map(list, partial_map)]))
    return my_map


def count_points(part):
    points = 0

    col_pairs = []
    row_pairs = []

    # Find matching cols
    for idx, col in enumerate(part[0]):
        try:
            if np.array_equal(part[:, idx + 1], part[:, idx]):
                # print("Founds pair:", idx+1, idx)
                col_pairs.append([idx + 1, idx])
        except IndexError:
            continue

    # Validate pairs
    valid_pair_indices = validate_pairs(col_pairs, part)

    if np.any(valid_pair_indices):
        col_pairs = np.array(col_pairs)
        valid_pair_indices = np.array(valid_pair_indices)
        # print("col points", col_pairs[valid_pair_indices][0][0])
        points += col_pairs[valid_pair_indices][0][0]

    valid_pair_indices = []

    # Find matching rows
    for idx, row in enumerate(part):
        try:
            if np.array_equal(part[idx + 1, :], part[idx, :]):
                # print("Founds pair:", idx+1, idx)
                row_pairs.append([idx + 1, idx])
        except IndexError:
            continue
        # print(part[idx, :])

    # Validate row pairs
    valid_pair_indices = validate_pairs(row_pairs, part.T)
    # print(valid_pair_indices)

    if np.any(valid_pair_indices):
        row_pairs = np.array(row_pairs)
        valid_pair_indices = np.array(valid_pair_indices)
        # print("rows points", row_pairs[valid_pair_indices][0][0])
        points += row_pairs[valid_pair_indices][0][0] * 100
    return points


def solve_part1(lines):
    my_map = parse_map(lines)
    points = 0
    for part in my_map:
        points += count_points(part)

    print("Part 1:", points)

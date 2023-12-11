from itertools import combinations

import numpy as np


def expand_space(space_map, expand_by=1):
    """
    Expand space map by duplicating rows and columns without galaxies.
    1. find rows without # => insert a row after them
    2. find cols without # => insert a col after them
    """
    empty_space_mask = space_map == "."
    rows_duplication_cond = np.all(empty_space_mask, axis=1)
    cols_duplication_cond = np.all(empty_space_mask, axis=0)
    row_indices = np.where(rows_duplication_cond)[0]
    duplicated_rows = space_map[rows_duplication_cond]
    expanded_space = np.insert(space_map, row_indices + 1, duplicated_rows, axis=0)
    for counter in range(expand_by-1):
        if counter % 1000 == 0:
            print("expanding rows", counter / expand_by * 100, "%")
        expanded_space = np.insert(expanded_space, row_indices + 1, duplicated_rows, axis=0)

    col_indices = np.where(cols_duplication_cond)[0]
    duplicated_cols = expanded_space[:, cols_duplication_cond]
    expanded_space = np.insert(expanded_space, col_indices + 1, duplicated_cols, axis=1)
    for counter in range(expand_by-1):
        if counter % 1000 == 0:
            print("expanding cols", counter / expand_by * 100, "%")
        expanded_space = np.insert(expanded_space, col_indices + 1, duplicated_cols, axis=1)

    return expanded_space.tolist()


def get_step_count(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def solve_part1(lines):
    space_map = np.array([list(line.strip()) for line in lines])
    expanded_space = np.array(expand_space(space_map))
    pairs = np.array(
        [*combinations(np.stack(np.where(expanded_space == "#"), axis=-1), 2)]
    )

    print("expanded_space shape", expanded_space.shape)
    print("pair count", len(pairs))

    steps = np.array([get_step_count(*pair) for pair in pairs])
    print(steps.sum())

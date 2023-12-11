from itertools import combinations

import numpy as np


def expand_space(space_map):
    empty_space_mask = space_map == "."
    rows_duplication_cond = np.all(empty_space_mask, axis=1)
    cols_duplication_cond = np.all(empty_space_mask, axis=0)
    row_indices = np.where(rows_duplication_cond)[0]
    duplicated_rows = space_map[rows_duplication_cond]
    expanded_space = np.insert(space_map, row_indices + 1, duplicated_rows, axis=0)
    col_indices = np.where(cols_duplication_cond)[0]
    duplicated_cols = expanded_space[:, cols_duplication_cond]
    expanded_space = np.insert(expanded_space, col_indices + 1, duplicated_cols, axis=1)
    return expanded_space.tolist()


def solve_part1(lines):
    space_map = np.array([list(line.strip()) for line in lines])
    # 1. find rows without # => insert a row after them
    # 2. find cols without # => insert a col after them
    expanded_space = np.array(expand_space(space_map))
    pairs = np.array([*combinations(np.stack(np.where(expanded_space == "#"), axis=-1), 2)])

    print(expanded_space)
    print(pairs)

    # 3. collect galaxies
    # 4. iterate on the galaxies:
    #    1. get the distance from all the other galaxies (row dist + col dist)
    # 5. sum up the distances/2

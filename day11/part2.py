from itertools import combinations

import numpy as np

from part1 import get_step_count


def expanded_coords(galaxy_coords, empty_row_indices, empty_col_indices, expand_by=1):
    updated_coords = []
    for coord in galaxy_coords:
        empty_rows_above = np.sum(coord[0] > empty_row_indices)
        empty_cols_left = np.sum(coord[1] > empty_col_indices)
        updated_coords.append(
            (
                coord[0] + empty_rows_above * expand_by,
                coord[1] + empty_cols_left * expand_by,
            )
        )
    return np.array(updated_coords)


def solve_part2(lines):
    space_map = np.array([list(line.strip()) for line in lines])
    galaxy_coords = np.stack(np.where(space_map == "#"), axis=-1)
    empty_row_indices = np.where(np.all(space_map == ".", axis=1))
    empty_col_indices = np.where(np.all(space_map == ".", axis=0))

    expanded_space = expanded_coords(
        galaxy_coords, empty_row_indices, empty_col_indices, expand_by=(1000000 - 1)
    )
    pairs = np.array([*combinations(expanded_space, 2)])

    steps = np.array([get_step_count(*pair) for pair in pairs])
    print(steps.sum())

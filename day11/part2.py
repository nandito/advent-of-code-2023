from itertools import combinations

import numpy as np
from part1 import expand_space, get_step_count


def solve_part2(lines):
    space_map = np.array([list(line.strip()) for line in lines])
    expanded_space = np.array(expand_space(space_map, expand_by=1000000))
    pairs = np.array(
        [*combinations(np.stack(np.where(expanded_space == "#"), axis=-1), 2)]
    )

    # print(expanded_space)
    # print(len(pairs))

    steps = np.array([get_step_count(*pair) for pair in pairs])
    print(steps.sum())

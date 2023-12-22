import numpy as np

from part1 import drop, parse_lines


def solve_part2(lines):
    bricks = parse_lines(lines)
    # print(bricks)

    drop(bricks)
    return np.sum([drop(bricks.copy(), skip=i) for i in range(len(bricks))], axis=0)[1]

import numpy as np


DIRECTIONS = {
    "-": np.array([[0, 1], [0, -1]]),
    "|": np.array([[1, 0], [-1, 0]]),
    "L": np.array([[0, 1], [-1, 0]]),
    "J": np.array([[-1, 0], [0, -1]]),
    "7": np.array([[0, -1], [1, 0]]),
    "F": np.array([[1, 0], [0, 1]]),
    "S": np.array([[1, 0], [0, 1], [-1, 0], [0, -1]]),
    ".": np.array([[0, 0]]),
}


def find_possible_direction(prev_pos, pos, maze, tile):
    tile = maze[pos[0], pos[1]]
    # print(f"\npos {pos}, tile {tile}, prev_pos {prev_pos}")
    options = DIRECTIONS[tile]
    next_pos = None
    for option in options:
        # print("!!!! option", option)
        next_row = pos[0] + option[0]
        next_col = pos[1] + option[1]
        if np.array_equal(prev_pos, [next_row, next_col]):
            # print("Skipping option going back", option)
            continue
        if next_row < 0 or next_col < 0:
            # print("Skipping option going out of bounds", option)
            continue
        # print("next_row,next_col", next_row, next_col)
        next_pos_tile = maze[next_row, next_col]
        # print("next_pos_tile", next_pos_tile)
        next_pos_option = DIRECTIONS[next_pos_tile]
        # print("next_pos_option before", next_pos_option)
        if next_pos_tile == ".":
            # print("Skipping option going to a ground", option)
            continue
        prelen = len(next_pos_option)
        next_pos_option = np.array(
            [
                subarr
                for subarr in next_pos_option
                if not np.array_equal(subarr, -option)
            ]
        )
        prolen = len(next_pos_option)
        if len(next_pos_option) == 0:
            # print("Skipping option that goes nowhere", option)
            continue
        if prelen == prolen:
            # print("Skipping option that doesn't connect", option)
            continue

        next_pos = [next_row, next_col]
    # print("next_options", next_options[-1])
    # print("next_pos", next_pos)
    return pos, next_pos, tile


def solve_part1(lines):
    maze = np.array([list(line.strip()) for line in lines])
    print(maze)
    pos = np.argwhere(maze == "S")[0]
    next_pos = pos
    steps = 0
    tile = maze[pos[0], pos[1]]

    while True:
        if tile == "S" and steps > 1:
            print("Found S again, steps", steps)
            break

        steps += 1
        pos, next_pos, tile = find_possible_direction(pos, next_pos, maze, tile="S")

    print((steps - 1) / 2)

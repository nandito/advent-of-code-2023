import numpy as np


# Define 2D grid of tiles' directions
DIRECTIONS = {
    "-": np.array([[ 0, 1 ], [ 0, -1 ]]),
    "|": np.array([[ 1, 0 ], [ -1, 0 ]]),
    "L": np.array([[ 0, 1 ], [ -1, 0 ]]),
    "J": np.array([[ -1, 0 ], [ 0, -1 ]]),
    "7": np.array([[ 0, -1 ], [ 1, 0 ]]),
    "F": np.array([[ 1, 0 ], [ 0, 1 ]]),
    "S": np.array([[ 1, 0 ], [ 0, 1 ], [ -1, 0 ], [ 0, -1 ]]),
    ".": np.array([[ 0, 0 ]]),
}



# Check surrounding tiles: left: -, L, F; right: -, J, 7, up: |, 7, F; down: |, J, L

# If tile is found, move to it and repeat and save the next direction

# If tile is S again, stop and print the directions


def find_possible_direction(prev_pos, pos, maze, tile):
    tile = maze[pos[0], pos[1]]
    # print(f"\npos {pos}, tile {tile}, prev_pos {prev_pos}")
    options = DIRECTIONS[tile]
    next_options = []
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
        next_pos_option = np.array([subarr for subarr in next_pos_option if not np.array_equal(subarr, -option)])
        prolen = len(next_pos_option)
        # print("next_pos_option after", next_pos_option)
        if len(next_pos_option) == 0:
            # print("Skipping option that goes nowhere", option)
            continue
        if prelen == prolen:
            # print("Skipping option that doesn't connect", option)
            continue

        # print("next_pos_option", next_pos_option)
        # print("pos", pos)
        next_pos = [next_row, next_col]
        # print("current next_pos", next_pos)

        # next_options.append(next_option)
    # print("next_options", next_options[-1])
    # print("next_pos", next_pos)
    return pos, next_pos, tile

def solve_part1(lines):
    maze = np.array([list(line.strip()) for line in lines])
    print(maze)
    # Find "S" position
    # s_pos = np.argwhere(maze == "S")[0]
    pos = np.argwhere(maze == "S")[0]
    next_pos = pos
    # possible_dir = find_possible_direction(s_pos, s_pos, maze)
    steps = 0
    # found = False
    # finished = False
    tile = maze[pos[0], pos[1]]

    while True:
        if tile == "S" and steps > 1:
            print("Found S again, steps", steps)
            break

        steps += 1
        pos, next_pos, tile = find_possible_direction(pos, next_pos, maze, tile="S")
        # print("pos", pos, "next_pos", next_pos, "steps", steps, tile)
        # if steps > 20:
        #     break

    # print(int(possible_dir / 2))
    print((steps-1) / 2)
    pass

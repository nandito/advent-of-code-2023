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


def find_possible_direction(pos, maze, steps=0):
    tile = maze[pos[0], pos[1]]
    print(f"\npos {pos}, tile {tile}, steps {steps}")
    if tile == "S" and steps > 0:
        return steps
    options = DIRECTIONS[tile]
    next_options = []
    for option in options:
        next_row = pos[0] + option[0]
        next_col = pos[1] + option[1]
        next_pos_tile = maze[next_row, next_col]
        next_pos_option = DIRECTIONS[next_pos_tile]
        if next_pos_tile == ".":
            continue
        next_pos_option = np.array([subarr for subarr in next_pos_option if not np.array_equal(subarr, -option)])
        if len(next_pos_option) == 0:
            continue

        next_option = DIRECTIONS[next_pos_tile]
        next_options.append(next_option)
    # print("\n\noptions", options)
    print("next_options", next_options[-1])
    # TODO: next_options should be a coord in the maze, not a direction
    next_pos = pos + next_options[-1][0]
    print("next_pos", next_pos)
    return find_possible_direction(next_pos, maze, steps + 1)
    # return find_possible_direction(next_options[0], maze, steps + 1)

def solve_part1(lines):
    maze = np.array([list(line.strip()) for line in lines])
    print(maze)
    # Find "S" position
    s_pos = np.argwhere(maze == "S")[0]
    possible_dir = find_possible_direction(s_pos, maze)
    pass

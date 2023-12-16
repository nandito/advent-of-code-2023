import numpy as np


DIRECTIONS = {"left": [0, -1], "up": [-1, 0], "right": [0, 1], "down": [1, 0]}


def get_directions(current_char, current_direction):
    next_directions = []
    if current_char == ".":
        # continue to the same direction
        next_directions.append(current_direction)
    elif current_char == "\\":
        # change direction to
        #   down if it was right
        #   up if it was left
        #   left if it was up
        #   right if it was down
        if current_direction == DIRECTIONS["down"]:
            next_directions.append(DIRECTIONS["right"])
        if current_direction == DIRECTIONS["up"]:
            next_directions.append(DIRECTIONS["left"])
        if current_direction == DIRECTIONS["right"]:
            next_directions.append(DIRECTIONS["down"])
        if current_direction == DIRECTIONS["left"]:
            next_directions.append(DIRECTIONS["up"])
    elif current_char == "/":
        # change direction to
        #   right => up
        #   left => down
        #   down => left
        #   up => right
        if current_direction == DIRECTIONS["right"]:
            next_directions.append(DIRECTIONS["up"])
        if current_direction == DIRECTIONS["left"]:
            next_directions.append(DIRECTIONS["down"])
        if current_direction == DIRECTIONS["down"]:
            next_directions.append(DIRECTIONS["left"])
        if current_direction == DIRECTIONS["up"]:
            next_directions.append(DIRECTIONS["right"])
    elif current_char == "|":
        # up => up, down => down
        # left or right => up + down
        if (
            current_direction == DIRECTIONS["left"]
            or current_direction == DIRECTIONS["right"]
        ):
            next_directions.append(DIRECTIONS["up"])
            next_directions.append(DIRECTIONS["down"])
        else:
            next_directions.append(current_direction)

    elif current_char == "-":
        # left => left, right => right
        # up or down => left + right
        if (
            current_direction == DIRECTIONS["up"]
            or current_direction == DIRECTIONS["down"]
        ):
            next_directions.append(DIRECTIONS["left"])
            next_directions.append(DIRECTIONS["right"])
        else:
            next_directions.append(current_direction)

    return next_directions


def solve_part1(lines):
    cave_map = [[*line.strip()] for line in lines]
    current_pos = np.array([0, 0])
    current_direction = DIRECTIONS["right"]
    existing_paths = [(current_pos.tolist(), current_direction)]
    beams = [(current_pos.tolist(), current_direction)]
    while len(beams) > 0:
        (current_pos, current_direction) = beams[0]
        beams.pop(0)
        current_char = cave_map[current_pos[0]][current_pos[1]]
        next_directions = get_directions(current_char, current_direction)
        for nd in next_directions:
            current_pos = np.array(current_pos) + np.array(nd)
            # print("current_pos", current_pos)
            if (
                current_pos[0] < 0
                or current_pos[0] >= len(cave_map)
                or current_pos[1] < 0
                or current_pos[1] >= len(cave_map[0])
            ):
                # print("beam ends")
                continue
            # elif if current_pos, nd is in beams, end
            elif (current_pos.tolist(), nd) in existing_paths:
                # print("beam already passed")
                pass
            else:
                beams.append((current_pos.tolist(), nd))

            existing_paths.append((current_pos.tolist(), nd))

    # print(existing_paths)
    visited_tiles = np.unique(np.array([*map(lambda b: b[0], existing_paths)]), axis=0)
    # print(visited_tiles)
    return len(visited_tiles)

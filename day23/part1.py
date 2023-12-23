import numpy as np

from collections import deque


def is_possible_slope(pos, last_pos, tile):
    pos_diff = np.array(pos) - np.array(last_pos)
    pos_diff = pos_diff.tolist()
    if pos_diff == [0, 1]:
        impossible_slope = "<"
    elif pos_diff == [0, -1]:
        impossible_slope = ">"
    elif pos_diff == [1, 0]:
        impossible_slope = "^"
    elif pos_diff == [-1, 0]:
        impossible_slope = "v"
    else:
        print("wrong dir?", pos_diff)

    # print(f"impossible_slope: {impossible_slope}, tile: {tile} tile is not impossible_slope: {tile != impossible_slope}")
    return tile != impossible_slope


def check_pos(trail, pos, last_slope, visited):
    tile_type = trail[pos[0]][pos[1]]
    pos = pos.tolist()
    if tile_type == "#":
        return False
    if pos in visited:
        return False
    if tile_type in ["<", ">", "v", "^"]:
        if not is_possible_slope(pos, visited[-1], tile_type):
            return False

    return pos


def get_possible_dirs(trail, position, last_slope, visited):
    # print(f"Get possible dirs for {position}")
    position = np.array(position)
    top = position + [-1, 0]
    bottom = position + [1, 0]
    left = position + [0, 1]
    right = position + [0, -1]
    possible_dirs = list(
        map(
            lambda p: check_pos(trail, p, last_slope, visited),
            [top, bottom, left, right],
        )
    )
    possible_dirs = list(filter(None, possible_dirs))

    return possible_dirs


def hike(trail):
    start_position = [0, trail[0].index(".")]
    last_position = [len(trail) - 1, trail[len(trail) - 1].index(".")]
    # print(last_position)
    possible_paths = []
    last_slope = None
    to_visit = deque([(start_position, [])])
    alt = deque([])
    counter = 0
    while len(to_visit) > 0 or len(alt) > 0:
        if len(to_visit) > 0:
            pos, visited = to_visit.popleft()
        else:
            pos, visited = alt.popleft()
            # print("deque", visited)
        visited.append(pos)

        # print("pos", pos)
        if pos == last_position:
            # print("last pos")
            possible_paths.append(visited)
            continue

        possible_dirs = get_possible_dirs(trail, pos, last_slope, visited)

        for idx, pd in enumerate(possible_dirs):
            if idx == 0:
                to_visit.append((pd, visited.copy()))
            else:
                alt.append((pd, visited.copy()))
        counter += 1
        if counter % 1000 == 0:
            print(f"iteration {counter}, alt paths: {len(alt)}")

    # print("to_visit", len(to_visit))
    # print("alt", len(alt))
    # print("possible_paths", len(possible_paths))

    # for pp in possible_paths:
    #     print("\nPath len:", len(pp) - 1)
    #     trail_copy = np.array(trail)
    #     for pos in pp:
    #         trail_copy[pos[0]][pos[1]] = "O"

    #     raw_string= '\n'.join([''.join(map(str, row)) for row in trail_copy])
    #     print(raw_string)

    return possible_paths


def solve_part1(lines):
    hiking_trail = [[*line.strip()] for line in lines]
    paths = hike(hiking_trail)

    return max(list(map(len, paths))) - 1

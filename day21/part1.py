from collections import deque

import numpy as np

# STEPS = 6
STEPS = 64


def solve_part1(lines):
    garden_map = np.array([list(line.strip()) for line in lines])
    start_pos = np.where(garden_map == "S")
    start_pos = (start_pos[0][0], start_pos[1][0])
    garden_map[start_pos[0], start_pos[1]] = "."
    garden_map = garden_map.tolist()

    # possible_moves = find_possible_moves(garden_map, start_pos)
    visited = {}
    to_visit = deque([(start_pos, 0)])
    while len(to_visit) > 0:
        coor, steps = to_visit.popleft()
        if coor in visited:
            continue
        if steps == (STEPS + 1):
            break
        visited[coor] = steps
        for add in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_coor = (coor[0] + add[0], coor[1] + add[1])
            try:
                if garden_map[new_coor[0]][new_coor[1]] == ".":
                    to_visit.append((new_coor, steps + 1))
            except IndexError:
                continue

    garden_map_copy = np.array(garden_map)
    for k, v in visited.items():
        if v % 2 == 0:
            garden_map_copy[k[0]][k[1]] = "O"

    print(str(garden_map_copy))

    count = sum([1 for v in visited.values() if v % 2 == 0])
    return count

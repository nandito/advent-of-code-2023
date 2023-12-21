import numpy as np


def find_possible_moves(garden_map, pos):
    possible_moves = []
    if garden_map[pos[0] - 1, pos[1]] == ".":
        possible_moves.append((pos[0] - 1, pos[1]))
    if garden_map[pos[0] + 1, pos[1]] == ".":
        possible_moves.append((pos[0] + 1, pos[1]))
    if garden_map[pos[0], pos[1] - 1] == ".":
        possible_moves.append((pos[0], pos[1] - 1))
    if garden_map[pos[0], pos[1] + 1] == ".":
        possible_moves.append((pos[0], pos[1] + 1))
    return possible_moves



def solve_part1(lines):
    garden_map = np.array([list(line.strip()) for line in lines])
    start_pos = np.where(garden_map == "S")
    garden_map[start_pos[0], start_pos[1]] = "."

    possible_moves = find_possible_moves(garden_map, start_pos)
    
    steps = 2
    step_options = [possible_moves]
    while steps < 7:
        print(f"Step {steps}")
        # print("step_options", step_options)
        garden_map_copy = garden_map.copy()
        for step_option in step_options:
            for step in step_option:
                garden_map_copy[step[0], step[1]] = "O"
        # print(garden_map_copy)
        new_step_options = []
        for step_option in step_options:
            for step in step_option:
                new_step_options.append(find_possible_moves(garden_map, step))

        step_options = new_step_options

        steps += 1

    garden_map_copy = garden_map.copy()
    for step_option in step_options:
        for step in step_option:
            garden_map_copy[step[0], step[1]] = "O"
    count = np.count_nonzero(garden_map_copy == "O")
    print(count)

    pass

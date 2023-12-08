import re

import pandas as pd


def walk(node_map, current_node, current_direction):
    return node_map.loc[current_node, current_direction]


def solve_part1(lines):
    directions = []
    NODE_MAP_REGEX = r"(\w{3})"
    node_map = pd.DataFrame(columns=["node", "L", "R"])

    for idx, line in enumerate(lines):
        if idx == 0:
            directions = [*line.strip()]
            continue

        match = re.findall(NODE_MAP_REGEX, line)
        if match:
            node_map.loc[len(node_map)] = match
            continue

    node_map.set_index("node", inplace=True)

    current_node = "AAA"
    step_count = 0
    direction_index = 0
    while True:
        step_count += 1
        # print(f"Current node: {current_node}, direction: {directions[direction_index]}, step count: {step_count}, direction_index: {direction_index}")
        current_direction = directions[direction_index]
        current_node = walk(node_map, current_node, current_direction)
        if current_node == "ZZZ":
            break
        if direction_index == len(directions) - 1:
            direction_index = 0
        else:
            direction_index += 1

    print(f"Part 1: {step_count}")

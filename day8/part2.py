import re

import pandas as pd

from math import lcm


def walk(node_map, current_node, current_direction):
    return node_map.loc[current_node, current_direction]


def solve_part2(lines):
    directions = []
    NODE_MAP_REGEX = r"(\w{3})"
    node_map = pd.DataFrame(columns=["node", "L", "R"])
    current_nodes = []

    for idx, line in enumerate(lines):
        if idx == 0:
            directions = [*line.strip()]
            continue

        match = re.findall(NODE_MAP_REGEX, line)
        if match:
            node_map.loc[len(node_map)] = match
            if match[0][-1] == "A":
                current_nodes.append(match[0])
            continue

    node_map.set_index("node", inplace=True)
    # print(current_nodes)

    step_counts = {idx: 0 for idx in range(len(current_nodes))}
    direction_index = 0

    for idx, current_node in enumerate(current_nodes):
        while True:
            step_counts[idx] += 1
            # print(
            #     f"Current node: {current_node}, direction: {directions[direction_index]}, step count: {step_counts}, direction_index: {direction_index}"
            # )
            current_direction = directions[direction_index]
            current_node = walk(node_map, current_node, current_direction)

            if current_node.endswith("Z"):
                direction_index = 0
                break

            if direction_index == len(directions) - 1:
                direction_index = 0
            else:
                direction_index += 1

    solution = lcm(*list(step_counts.values()))
    print(f"Part 2: {solution}")

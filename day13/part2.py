import numpy as np
from part1 import parse_map, count_points


def flip_cell(cell):
    if cell == ".":
        return "#"
    elif cell == "#":
        return "."
    else:
        raise ValueError(f"Invalid cell: {cell}")


def solve_part2(lines):
    my_map = parse_map(lines)
    points = 0
    for part in my_map:
        current_points = 0
        for idx, row in enumerate(part):
            for jdx, cell in enumerate(row):
                part[idx][jdx] = flip_cell(cell)
                current_points = count_points(part)
                print(part)
                # print(current_points)
                if current_points > 0:
                    break
            if current_points > 0:
                break

        # while current_points == 0:
        #     # apply flip_cell to each cell, one at a time
        #     part = np.rot90(part)
        #     current_points = count_points(part)
        #     print(current_points)
        #     steps += 1
        #     if steps > 20:
        #         break
        points += current_points

    print("Part 2:", points)
    pass

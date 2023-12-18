import re

import numpy as np
import shapely


def make_line(pos, pos2):
    try:
        return shapely.LineString([pos, pos2])
    except KeyError:
        return None


def dig_trench(dig_plan):
    position = np.array([0, 0])
    next_position = np.array([0, 0])
    lines = []
    for direction, step, color in dig_plan:
        if direction == "R":
            next_position = position + [0, step]
        elif direction == "L":
            next_position = position + [0, -step]
        elif direction == "U":
            next_position = position + [-step, 0]
        elif direction == "D":
            next_position = position + [step, 0]
        lines.append(make_line(position, next_position))
        position = next_position

    # print(lines)
    merged = shapely.line_merge(shapely.union_all(lines))
    poly = shapely.Polygon(merged)
    # print(merged)
    # print(merged.length)
    # print(merged.area)
    # print(poly)
    # print(poly.length)
    # print(poly.area)
    return poly.area + (poly.length / 2) + 1


def solve_part1(lines):
    dig_plan = list(
        map(
            lambda r: (r[0], int(r[1]), re.sub(r"[()]", "", r[2])),
            [line.strip().split() for line in lines],
        )
    )
    # print(dig_plan)
    size = dig_trench(dig_plan)
    return size

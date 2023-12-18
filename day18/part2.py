import re

from part1 import dig_trench

dirs = ["R", "D", "L", "U"]


def parse_instructions(line):
    raw = re.sub(r"[()#]", "", line[2])
    # print(raw)
    direction = dirs[int(raw[5])]
    steps = int(raw[0:5], base=16)
    return (direction, steps, "noop")


def solve_part2(lines):
    dig_plan = list(
        map(
            parse_instructions,
            [line.strip().split() for line in lines],
        )
    )
    # print(dig_plan)
    size = dig_trench(dig_plan)
    return size

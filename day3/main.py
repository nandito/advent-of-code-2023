import argparse

import numpy as np

from part1 import solve_part1
from part2 import solve_part2

parser = argparse.ArgumentParser(
    description="Advent of Code 2023 - Day 3",
    epilog="https://adventofcode.com/2023/day/3",
)
parser.add_argument(
    "-i",
    "--input_file",
    metavar="FILE",
    type=str,
    help="The input file containing the puzzle input",
    required=True,
)
parser.add_argument(
    "-p",
    "--part",
    choices=["1", "2"],
    help="The part of the puzzle to solve",
    required=True,
)

args = parser.parse_args()

with open(args.input_file) as f:
    m = np.array([])
    for file_line in f:
        m = np.array([*m, [*file_line.strip()]])
    if args.part == "1":
        solve_part1(m)
    elif args.part == "2":
        solve_part2(m)
    else:
        print("Invalid part specified")
        exit(1)

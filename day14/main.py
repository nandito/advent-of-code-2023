import argparse
import time

from part1 import solve_part1
from part2 import solve_part2

parser = argparse.ArgumentParser(
    description="Advent of Code 2023 - Day 14",
    epilog="https://adventofcode.com/2023/day/14",
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
    start = time.time()
    if args.part == "1":
        result = solve_part1(f)
    elif args.part == "2":
        result = solve_part2(f)
    else:
        print("Invalid part specified")
        exit(1)
    end = time.time()
    print(f"Part {args.part}: {result}")
    print("It took {:.2f} s to compute".format(end - start))

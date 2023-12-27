from part1 import get_arrangement_count


def solve_part2(lines):
    condition_records = [list(line.strip().split(" ")) for line in lines]
    condition_records = [
        (p1, tuple(map(int, p2.split(",")))) for p1, p2 in condition_records
    ]
    solution = [
        get_arrangement_count("?".join([group] * 5) + ".", size * 5) for group, size in condition_records
    ]
    print("Part 2:", sum(solution))

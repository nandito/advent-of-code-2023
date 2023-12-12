def get_arrangement_count(group, sizes, num_done_in_group=0):
    if not group:
        return not sizes and not num_done_in_group

    solution_count = 0
    # If the next letter is "?" we go on a new branch
    possible = [".", "#"] if group[0] == "?" else group[0]
    # print(f"group: {group}, sizes: {sizes}, num_done_in_group: {num_done_in_group}")
    for character in possible:
        if character == "#":
            # Extend current group
            solution_count += get_arrangement_count(
                group[1:], sizes, num_done_in_group + 1
            )
        else:
            if num_done_in_group:
                # When group can be closed, close it
                if sizes and sizes[0] == num_done_in_group:
                    solution_count += get_arrangement_count(group[1:], sizes[1:])
            else:
                # Move to the next character if not in a group
                solution_count += get_arrangement_count(group[1:], sizes)

    return solution_count


def solve_part1(lines):
    condition_records = [list(line.strip().split(" ")) for line in lines]
    condition_records = [
        (p1, tuple(map(int, p2.split(",")))) for p1, p2 in condition_records
    ]
    solution = [
        get_arrangement_count(group + ".", size) for group, size in condition_records
    ]
    print("Part 1:", sum(solution))

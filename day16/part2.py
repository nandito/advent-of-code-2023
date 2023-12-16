from part1 import DIRECTIONS, get_visited_tile_count


def get_entries(cave_map):
    row_count = len(cave_map)
    col_count = len(cave_map[0])
    first_row_entries = [([0, idx], DIRECTIONS["down"]) for idx in range(0, row_count)]
    last_row_entries = [
        ([row_count - 1, idx], DIRECTIONS["up"]) for idx in range(0, row_count)
    ]
    first_col_entries = [([idx, 0], DIRECTIONS["right"]) for idx in range(0, col_count)]
    last_col_entries = [
        ([idx, col_count - 1], DIRECTIONS["left"]) for idx in range(0, col_count)
    ]
    return first_row_entries + last_row_entries + first_col_entries + last_col_entries


def solve_part2(lines):
    cave_map = [[*line.strip()] for line in lines]
    visited_tile_counts = []
    entry_points = get_entries(cave_map)
    it = 0
    for starting_pos, starting_direction in entry_points:
        # print(f"iteration: {it}, starting_pos: {starting_pos}, starting_direction: {starting_direction}")
        visited_tile_count = get_visited_tile_count(
            cave_map, starting_pos, starting_direction
        )
        visited_tile_counts.append(visited_tile_count)
        it += 1
        # if it%10 == 0:
        #     print(f"visited_tile_counts: {visited_tile_counts}")

    return max(visited_tile_counts)

from itertools import combinations

import shapely

TEST_AREA = [7, 27]
# TEST_AREA = [200000000000000, 400000000000000]


def get_intersection_point(stone1, stone2):
    pos1 = stone1[0][:2]
    vel1 = stone1[1]
    pos2 = stone2[0][:2]
    vel2 = stone2[1]
    # print(pos1, pos2)

    time_elapsed = 1
    has_intersection = False
    intersection = None
    while not has_intersection:
        pos1f = [pos1[0] + vel1[0] * time_elapsed, pos1[1] + vel1[1] * time_elapsed]
        pos2f = [pos2[0] + vel2[0] * time_elapsed, pos2[1] + vel2[1] * time_elapsed]

        # :shrug:
        if (
            pos1[0] < 0
            or pos1[1] < 0
            or pos1f[0] < 0
            or pos1f[1] < 0
            or pos2[0] < 0
            or pos2[1] < 0
            or pos2f[0] < 0
            or pos2f[1] < 0
        ):
            break

        line1 = shapely.LineString([pos1, pos1f])
        line2 = shapely.LineString([pos2, pos2f])
        # print(line1, line2)
        if shapely.intersects(line1, line2):
            has_intersection = True
            intersection = shapely.intersection(line1, line2)
            # print("has_intersection after time_elapsed", time_elapsed)
        # if time_elapsed > 100:
        # break

        time_elapsed += 1

    # print(intersection)
    return intersection


def is_in_range(point):
    if not point:
        return False

    return (
        point.x > TEST_AREA[0]
        and point.x < TEST_AREA[1]
        and point.y > TEST_AREA[0]
        and point.y < TEST_AREA[1]
    )


def solve_part1(lines):
    hailstone_states = []
    for line in lines:
        line_parts = []
        for part in line.strip().split("@"):
            values = list(map(int, part.split(",")))
            line_parts.append(values)
        hailstone_states.append(line_parts)

    pairs = list(combinations(hailstone_states, 2))

    # get_intersection_point(pairs[0][0], pairs[0][1])

    intersections = list(
        map(lambda pair: get_intersection_point(pair[0], pair[1]), pairs)
    )

    # print(intersections)

    inside_test_area = list(map(is_in_range, intersections))
    return inside_test_area.count(True)

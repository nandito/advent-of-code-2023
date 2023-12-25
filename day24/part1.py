from itertools import combinations

import shapely

# TEST_AREA = [7, 27]
TEST_AREA = [200000000000000, 400000000000000]


def get_intersection_point(stone1, stone2):
    pos1 = stone1[0][:2]
    vel1 = stone1[1]
    pos2 = stone2[0][:2]
    vel2 = stone2[1]
    # print(pos1, pos2)

    pos1f = [pos1[0] + vel1[0] * TEST_AREA[1], pos1[1] + vel1[1] * TEST_AREA[1]]
    pos2f = [pos2[0] + vel2[0] * TEST_AREA[1], pos2[1] + vel2[1] * TEST_AREA[1]]

    line1 = shapely.LineString([pos1, pos1f])
    line2 = shapely.LineString([pos2, pos2f])
    intersection = None
    # print(line1, line2)
    if shapely.intersects(line1, line2):
        intersection = shapely.intersection(line1, line2)

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

    intersections = list(
        map(lambda pair: get_intersection_point(pair[0], pair[1]), pairs)
    )

    # print(intersections)

    inside_test_area = list(map(is_in_range, intersections))
    return inside_test_area.count(True)

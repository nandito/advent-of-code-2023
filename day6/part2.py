import re
import numpy as np


def get_possible_distances(time):
    distances = []
    for ms in range(1, time):
        distances.append((time - ms) * ms)
    return distances


def parse_input(input):
    TIME_REGEX = r"Time:\s*(\d+(?:\s*\d*)*)"
    DISTANCE_REGEX = r"Distance:\s*(\d+(?:\s*\d*)*)"
    time = None
    distance_record = None

    for line in input:
        time_row = re.match(TIME_REGEX, line)
        distance_row = re.match(DISTANCE_REGEX, line)
        if time_row:
            time = int("".join(time_row.group(1).split()))
        if distance_row:
            distance_record = int("".join(distance_row.group(1).split()))
    return [time, distance_record]


def get_record_breakers_count(time, distance_record):
    distances = np.array(get_possible_distances(time))
    record_breakers = distances[distances > distance_record]
    return len(record_breakers)


def solve_part2(input):
    [time, distance_record] = parse_input(input)
    record_breakers_count = get_record_breakers_count(time, distance_record)
    print("Times: ", time)
    print("Distance records: ", distance_record)
    print("Record breakers_count: ", record_breakers_count)

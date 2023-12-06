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
    times = None
    distance_records = None

    for line in input:
        time_row = re.match(TIME_REGEX, line)
        distance_row = re.match(DISTANCE_REGEX, line)
        if time_row:
            times = [int(t) for t in time_row.group(1).split()]
        if distance_row:
            distance_records = [int(d) for d in distance_row.group(1).split()]
    return [times, distance_records]


def get_record_breakers_count(times, distance_records):
    record_breaker_count = []

    for idx, t in enumerate(times):
        distances = np.array(get_possible_distances(t))
        record_breakers = distances[distances > distance_records[idx]]
        record_breaker_count.append(len(record_breakers))
        # record_breakers.append(distances[distances > distance_records[idx]])
    return np.product(record_breaker_count)


def solve_part1(input):
    [times, distance_records] = parse_input(input)
    record_breakers_count = get_record_breakers_count(times, distance_records)
    print("Times: ", times)
    print("Distance records: ", distance_records)
    print("Record breakers_count: ", record_breakers_count)

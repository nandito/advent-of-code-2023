import numpy as np
from joblib import Memory

from part1 import sum_up, tilt

location = "./cachedir"
memory = Memory(location, verbose=0)


def tilt_cycle(rows):
    rows = np.array(rows)
    north = np.rot90(np.array(list(map(tilt, np.rot90(rows)))), k=3)
    west = np.array(list(map(tilt, north)))
    south = np.rot90(np.array(list(map(tilt, np.rot90(west, k=3)))), k=1)
    east = np.rot90(np.array(list(map(tilt, np.rot90(south, k=2)))), k=2)
    return east


def solve_part2(lines):
    rows = np.array([[*line.strip()] for line in lines]).tolist()
    period = transient = t = 0
    tilted_rows = rows
    states = [rows]
    cached_tilt_cycle = memory.cache(tilt_cycle)
    target = 1_000_000_000
    while True:
        tilted_rows = cached_tilt_cycle(states[t]).tolist()
        if tilted_rows in states:
            transient = states.index(tilted_rows)
            period = t + 1 - transient
            break
        states.append(tilted_rows)
        t += 1

    total = sum_up(states[(target - transient) % period + transient])
    return total

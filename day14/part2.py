import time

import numpy as np
from joblib import Memory

from part1 import tilt

location = "./cachedir"
memory = Memory(location, verbose=0)


def tilt_cycle(rows):
    north = np.rot90(np.array(list(map(tilt, np.rot90(rows)))), k=3)
    west = np.array(list(map(tilt, north)))
    south = np.rot90(np.array(list(map(tilt, np.rot90(west, k=3)))), k=1)
    east = np.rot90(np.array(list(map(tilt, np.rot90(south, k=2)))), k=2)
    return east


def solve_part2(lines):
    rows = np.array([[*line.strip()] for line in lines])
    # cycled = tilt_cycle(rows)
    # cycled = tilt_cycle(cycled)
    tilted_rows = rows
    cached_tilt_cycle = memory.cache(tilt_cycle)
    start = time.time()
    # for i in range(100000):
    for i in range(1000000000):
        if i % 10000 == 0:
            current_time = time.time()
            print(
                "It took {:.2f} s to compute ".format(current_time - start)
                + str(i)
                + " iteration"
            )
        tilted_rows = cached_tilt_cycle(tilted_rows)

    end = time.time()
    print("cycles took {:.2f} s to compute".format(end - start))

    print(tilted_rows)

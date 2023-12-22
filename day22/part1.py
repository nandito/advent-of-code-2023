import numpy as np


def drop(stack, skip=None):
    """
    :param stack: 2D array of bricks
    :param skip: index of brick to skip
    :return: (True if no falls, number of falls)

    1. Initialize a 2D numpy array `peaks` with zeros, having a shape of (12,
    12). This array will be used to keep track of peaks encountered during the
    iteration.

    2. Initialize a variable `falls` to 0. This variable will be used to count
    the number of falls during the iteration.

    3. Iterate through each element in the `stack` array using `enumerate`,
    where each element is a tuple `(u, v, w, x, y, z)`.

    4. Check if the current index `i` is equal to the value of `skip`. If so,
    skip the current iteration.

    5. Calculate the maximum value within the subarray of `peaks` defined by
    the coordinates `(u, v)` and `(x, y)`. This represents the maximum peak
    value in that region.

    6. Update the `peaks` array by setting the values in the specified region
    to the calculated peak value plus the difference between `z` and `w`.

    7. Update the current element in the `stack` array by replacing the values
    of `u`, `v`, and `z` with `u`, `v`, and the calculated peak value plus the
    difference between `z` and `w`.

    8. Increment the `falls` variable if the calculated peak value is less than
    `w`.

    9. Finally, the function returns a tuple with two values:
        - The first value is a boolean indicating whether there were no falls
          (`not falls`). If true, it means that all peaks were greater than or
          equal to their corresponding `w` values.
       - The second value is the count of falls (`falls`), representing the
         number of peaks that were less than their corresponding `w` values.
    """
    peaks = np.zeros((12, 12))
    falls = 0

    for i, (u, v, w, x, y, z) in enumerate(stack):
        if i == skip:
            continue

        peak = peaks[u:x, v:y].max()
        peaks[u:x, v:y] = peak + z - w

        stack[i] = u, v, peak, x, y, peak + z - w
        falls += peak < w

    return not falls, falls


def parse_lines(lines):
    bricks = []
    for line in lines:
        brick = []
        for p in line.split("~"):
            for c in p.split(","):
                brick.append(int(c))
        bricks.append(brick)
    bricks = np.array(bricks)
    bricks = bricks[bricks[:, 2].argsort()] + [0, 0, 0, 1, 1, 1]
    return bricks


def solve_part1(lines):
    bricks = parse_lines(lines)
    # print(bricks)

    drop(bricks)

    return np.sum([drop(bricks.copy(), skip=i) for i in range(len(bricks))], axis=0)[0]

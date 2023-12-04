import re
import numpy as np

with open("input") as f:
    lines = f.readlines()
    pattern = r"Card.*(\d+):\s*(\d+(?:\s*\d*)*)\s*\|\s*(\d+(?:\s*\d*)*)"
    points = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            card_number = int(match.group(1))
            winning_numbers = list(map(int, match.group(2).split()))
            my_numbers = list(map(int, match.group(3).split()))

            all_numbers = np.concatenate((winning_numbers, my_numbers))
            unique = np.unique(all_numbers)
            point_power = len(all_numbers)-len(unique) - 1
            result = pow(2, point_power) if point_power >= 0 else 0
            points.append(result)
        else:
            print("No match found.", line)

    print(sum(points))

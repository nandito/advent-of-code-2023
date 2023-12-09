import re

import numpy as np

with open("input") as f:
    lines = f.readlines()
    pattern = r"Card\s*(\d+):\s*(\d+(?:\s*\d*)*)\s*\|\s*(\d+(?:\s*\d*)*)"
    occurrence_map = {}
    for line in lines:
        match = re.match(pattern, line)
        if match:
            card_number = int(match.group(1))
            winning_numbers = list(map(int, match.group(2).split()))
            my_numbers = list(map(int, match.group(3).split()))
            # print("card_number", card_number, "winning_numbers", winning_numbers, "my_numbers", my_numbers)
            occurrence_map[card_number] = occurrence_map.get(card_number, 0) + 1

            all_numbers = np.concatenate((winning_numbers, my_numbers))
            unique = np.unique(all_numbers)
            winning_copy_count = len(all_numbers) - len(unique)

            occurrences = occurrence_map.get(card_number, 0)
            # print("\noccurrences", occurrences)
            for cn in range(1, winning_copy_count + 1):
                next_card_number = card_number + cn
                # print("---adding next_card_number", next_card_number)
                occurrence_map[next_card_number] = (
                    occurrence_map.get(next_card_number, 0) + occurrences
                )

        else:
            print("No match found.", line)

    # print("occurrence_map", occurrence_map)
    print("total scorecards", sum(occurrence_map.values()))

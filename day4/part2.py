import re
import numpy as np

with open("sample_input") as f:
    lines = f.readlines()
    pattern = r"Card.*(\d+):\s*(\d+(?:\s*\d*)*)\s*\|\s*(\d+(?:\s*\d*)*)"
    points = []
    scratchcards = np.array([])
    for line in lines:
        match = re.match(pattern, line)
        if match:
            card_number = int(match.group(1))
            winning_numbers = list(map(int, match.group(2).split()))
            my_numbers = list(map(int, match.group(3).split()))
            scratchcards = np.append(scratchcards, card_number)
            # print("scratchcards", scratchcards)

            all_numbers = np.concatenate((winning_numbers, my_numbers))
            unique = np.unique(all_numbers)
            winning_copy_count = len(all_numbers) - len(unique)
            # print("card_number:", card_number, "winning_copy_count", winning_copy_count)

            # count how many times we have card_number in scratchcards and run in x times
            occurrences = np.count_nonzero(scratchcards == card_number)
            # print("occurrences", occurrences)
            for o in range(0, occurrences):
                for cn in range(1, winning_copy_count + 1):
                    next_card_number = card_number + cn
                    # print("---adding next_card_number", next_card_number)
                    scratchcards = np.append(scratchcards, next_card_number)

        else:
            print("No match found.", line)

    # print("scratchcards", np.sort(scratchcards))
    print(len(scratchcards))
    # print(sum(points))

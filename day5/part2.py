import re

from part1 import process_mappings


with open("input") as f:
    lines = f.readlines()
    seeds_regex = r"seeds:\s*(\d+(?:\s*\d*)*)"
    map_regex = r"(\d+) (\d+) (\d+)"
    map_title_regex = r"(\w+)-\w+-(\w+)\smap:"

    numbers_to_match = []
    map = []

    for line in lines:
        if re.search(seeds_regex, line):
            # numbers_to_match = [ int(s) for s in re.search(seeds_regex, line).groups()[0].split() ]
            seed_ranges = [
                int(s) for s in re.search(seeds_regex, line).groups()[0].split()
            ]
            for idx, n in enumerate(seed_ranges):
                if idx % 2 == 0:
                    numbers_to_match.extend(range(n, n + seed_ranges[idx + 1]))

        elif re.search(map_title_regex, line):
            map_title = re.search(map_title_regex, line).groups()
            numbers_to_match = process_mappings(map, numbers_to_match)
            print("map_title", map_title)
            map = []

        elif re.search(map_regex, line):
            map_data = re.search(map_regex, line).groups()
            map = [*map, [int(map_data[0]), int(map_data[1]), int(map_data[2])]]

    # process last map
    numbers_to_match = process_mappings(map, numbers_to_match)

    print(min(numbers_to_match))

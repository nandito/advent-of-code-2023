import re


def process_mappings(map, numbers_to_match):
    destination_numbers = []

    for number in numbers_to_match:
        destination_number = None
        for target_start, source_start, source_length in map:
            if source_start <= number < source_start + source_length:
                destination_number = target_start + (number - source_start)
                break

        destination_numbers.append(destination_number or number)

    return destination_numbers


with open("input") as f:
    lines = f.readlines()
    seeds_regex = r"seeds:\s*(\d+(?:\s*\d*)*)"
    map_regex = r"(\d+) (\d+) (\d+)"
    map_title_regex = r"(\w+)-\w+-(\w+)\smap:"

    numbers_to_match = []
    map = []

    for line in lines:
        if re.search(seeds_regex, line):
            numbers_to_match = [
                int(s) for s in re.search(seeds_regex, line).groups()[0].split()
            ]
        elif re.search(map_title_regex, line):
            map_title = re.search(map_title_regex, line).groups()
            numbers_to_match = process_mappings(map, numbers_to_match)
            map = []

        elif re.search(map_regex, line):
            map_data = re.search(map_regex, line).groups()
            map = [*map, [int(map_data[0]), int(map_data[1]), int(map_data[2])]]

    # process last map
    numbers_to_match = process_mappings(map, numbers_to_match)

    print(min(numbers_to_match))

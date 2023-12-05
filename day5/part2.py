import re
import numpy as np

def get_subrange_left(dest, source):
    dest_start, dest_end = dest
    source_start, source_end = source
    subranges = []
    print("dest nums", [*range(dest_start, dest_end)])
    print("source nums", [*range(source_start, source_end)])
    dest_range = range(dest_start, dest_end)
    source_range = range(source_start, source_end)
    overlap_count = len(set(dest_range) & set(source_range))
    subranges.append([source_start, overlap_count])
    left_over_start = dest_start + overlap_count
    left_over_count = len(dest_range) - overlap_count
    subranges.append([left_over_start, left_over_count])
    
    return subranges

def get_subrange_right(dest, source):
    print(dest, source)
    dest_start, dest_end = dest
    source_start, source_end = source
    subranges = []
    print("dest nums", [*range(dest_start, dest_end)])
    print("source nums", [*range(source_start, source_end)])
    dest_range = range(dest_start, dest_end)
    source_range = range(source_start, source_end)
    overlap_count = len(set(dest_range) & set(source_range))
    ## TODO: fix this what to extract from dest_start
    left_over_start = dest_start - overlap_count
    print("left_over_start", left_over_start)
    left_over_count = len(dest_range) - overlap_count
    print("overlap_count", overlap_count)
    subranges.append([dest_end - overlap_count+1, left_over_count])
    print("left_over_count", left_over_count)
    # subranges.append([left_over_start, overlap_count])
    
    return subranges
    


def process_mappings(map, range_to_match):
    destination_numbers = []

    # create a pairs array. It should group range_to_match to 2 pairs of numbers
    # e.g. [1, 2, 3, 4] => [[1, 2], [3, 4]]
    print("range_to_match", range_to_match)
    pairs = []
    for i in range(0, len(range_to_match), 2):
        pairs.append([range_to_match[i], range_to_match[i + 1]])

    print("pairs", pairs)
    print("map", map)

    # for each pair, find the corresponding map
    for [dest_start, dest_len] in pairs:
        dest_end = dest_start + dest_len
        destination_pair = None
        destination_pairs = []
        for target_start, source_start, source_length in map:
            print("\ndest_start", dest_start, "dest_end", dest_end)
            print("source_start", source_start, "source_end", source_start + source_length)
            # if range has no overlap with map, skip
            if dest_end < source_start or dest_start >= source_start + source_length:
                print("range has no overlap with map, skip")
                continue 
            # if range is fully contained in map, map it
            if dest_start >= source_start and dest_end <= source_start + source_length:
                print("range is fully contained in map", dest_start, dest_end)
                # print("---pair", [dest_start, dest_len], "range", [source_start, source_length])
                new_source_start = target_start + (dest_start - source_start)
                destination_pair = [
                    new_source_start,
                    (target_start + (dest_end - source_start)) - new_source_start,
                ]
                destination_pairs.append(destination_pair)
                # print("destination_pair", destination_pair)
                break
            if dest_start > source_start and dest_end > source_start + source_length:
                print("!!   range is partially contained left", dest_start, dest_end)
                subranges = get_subrange_left([dest_start, dest_end], [source_start, source_start + source_length])
                # print("subranges", subranges)
                destination_pairs.extend(subranges)
                # print("destination_pairs", destination_pairs)
                break
            if dest_start < source_start and dest_end < source_start + source_length:
                print("!!   range is partially contained right", dest_start, dest_end)
                subranges = get_subrange_right([dest_start, dest_end], [source_start, source_start + source_length])
                print("subranges", subranges)
                destination_pairs.extend(subranges)
                print("destination_pairs", destination_pairs)
                break
            # if range is partially contained, add all partial ranges to destination_pairs
            # else:
            #     print("range is partially contained", dest_start, dest_end)
            #     new_source_start = target_start + (dest_start - source_start)
            #     destination_pair = [
            #         new_source_start,
            #         (target_start + (dest_end - source_start)) - new_source_start,
            #     ]
            #     print("destination_pair", destination_pair)
            #     break

            # print("no map found for range", dest_start, dest_end)
            # destination_pairs.append([dest_start, dest_len])

        # destination_numbers.extend(destination_pair or [dest_start, dest_len])
        # print("Adding")
        # print("destination_pair", destination_pair)
        # print("destination_pairs", destination_pairs)
        destination_numbers.extend(destination_pairs or [[dest_start, dest_len]])


    print("destination_numbers", destination_numbers)
    return np.array(destination_numbers).flatten().tolist()


# with open("sample_input") as f:
#     lines = f.readlines()
#     seeds_regex = r"seeds:\s*(\d+(?:\s*\d*)*)"
#     map_regex = r"(\d+) (\d+) (\d+)"
#     map_title_regex = r"(\w+)-\w+-(\w+)\smap:"

#     numbers_to_match = []
#     map = []

#     for line in lines:
#         if re.search(seeds_regex, line):
#             # numbers_to_match = [ int(s) for s in re.search(seeds_regex, line).groups()[0].split() ]
#             seed_ranges = [
#                 int(s) for s in re.search(seeds_regex, line).groups()[0].split()
#             ]
#             for idx, n in enumerate(seed_ranges):
#                 if idx % 2 == 0:
#                     numbers_to_match.extend(range(n, n + seed_ranges[idx + 1]))
#             print("numbers_to_match", numbers_to_match)

#         elif re.search(map_title_regex, line):
#             map_title = re.search(map_title_regex, line).groups()
#             numbers_to_match = process_mappings(map, numbers_to_match)
#             print("numbers_to_match", numbers_to_match)
#             print("map_title", map_title)
#             map = []

#         elif re.search(map_regex, line):
#             map_data = re.search(map_regex, line).groups()
#             map = [*map, [int(map_data[0]), int(map_data[1]), int(map_data[2])]]

#     # process last map
#     numbers_to_match = process_mappings(map, numbers_to_match)
#     print("numbers_to_match", numbers_to_match)

#     print(min(numbers_to_match))

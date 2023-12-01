number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 

def get_numbers(line):
    matches = dict()
    chars = [*line]
    for idx,c in enumerate(chars):
        if c.isdigit():
            if c in matches:
                matches[c] = [*matches[c], idx]
            else:
                matches[c] = [idx]
    return matches
                


def get_number_word(line):
    matches = dict()
    for idx,word in enumerate(number_words):
        word_matches = list(find_all(line,word))
        if len(word_matches):
            num = idx+1
            matches[num] = word_matches

    return matches

def find_smallest_index(dictionary):
    smallest_idx = 100000
    res = []
    for k,v in dictionary.items():
        for match in v:
            if match < smallest_idx:
                smallest_idx = match
                res = [str(k), match]
    return res

def find_largest_index(dictionary):
    largest_idx = -1
    res = []
    for k,v in dictionary.items():
        for match in v:
            if match > largest_idx:
                largest_idx = match
                res = [str(k), match]
    return res

def get_smaller_num(d1,d2):
    if len(d1) == 0:
        return d2[0]
    if len(d2) == 0:
        return d1[0]
    return d1[0] if d1[1] < d2[1] else d2[0]

def get_larger_num(d1,d2):
    if len(d1) == 0:
        return d2[0]
    if len(d2) == 0:
        return d1[0]
    return d1[0] if d1[1] > d2[1] else d2[0]


def get_string_and_digit_numbers(line):
    numbers = get_numbers(line)
    number_words = get_number_word(line) 
    smallest_number_word = find_smallest_index(number_words)
    smallest_number = find_smallest_index(numbers)
    smallest_digit = get_smaller_num(smallest_number, smallest_number_word)

    largest_number_word = find_largest_index(number_words)
    largest_number = find_largest_index(numbers)
    largest_digit = get_larger_num(largest_number, largest_number_word)
    # print(line, smallest_digit+largest_digit)
    # print("numbers:",numbers,"number_words:", number_words)
    # print("smallest_num_w:",smallest_number_word, "smallest_num:", smallest_number, "largest_num_w:",largest_number_word, "largest_num:",largest_number)
    return int(smallest_digit+largest_digit)
    

with open('input') as f:
    row_values = []
    for line in f:
        row_value = get_string_and_digit_numbers(line)
        row_values.append(row_value)
    sums = sum(row_values)
    print(sums)

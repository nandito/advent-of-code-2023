def hash_alg(code):
    current_val = 0
    for c in [*code]:
        ascii_code = ord(c)
        current_val += ascii_code
        current_val = 17 * current_val
        current_val = current_val % 256

    return current_val


def solve_part1(lines):
    codes = [[*line.split(",")] for line in lines][0]
    total = sum(map(hash_alg, codes))
    return total 

from part1 import hash_alg


def process_code(code, boxes):
    if "-" in code:
        code_id = code.split("-")[0]
        hash_value = hash_alg(code_id)
        matches = [v for v in boxes[hash_value] if v.startswith(code_id)]
        if len(matches) > 0:
            boxes[hash_value] = [
                v for v in boxes[hash_value] if not v.startswith(code_id)
            ]

    elif "=" in code:
        code_id, focal_length = code.split("=")
        hash_value = hash_alg(code_id)
        matches = [v for v in boxes[hash_value] if v.startswith(code_id)]
        if matches:
            boxes[hash_value] = [
                v.replace(matches[0], code_id + "=" + focal_length)
                for v in boxes[hash_value]
            ]
        else:
            boxes[hash_value].append(code_id + "=" + focal_length)

    return boxes


def sum_up_focusing_power(boxes):
    total = 0
    for box_idx, box in enumerate(boxes):
        for lens_idx, code in enumerate(box):
            code_id, focal_length = code.split("=")
            total += (box_idx + 1) * (lens_idx + 1) * int(focal_length)
    return total


def solve_part2(lines):
    boxes = [[] for _ in range(256)]
    codes = [[*line.split(",")] for line in lines][0]
    for code in codes:
        boxes = process_code(code, boxes)

    total = sum_up_focusing_power(boxes)
    return total

def has_adjacent_symbol(col, row, matrix):
    has_adjacent = False
    directions = [
        [-1, 0],  # left
        [1, 0],  # right
        [-1, -1],  # top left
        [0, -1],  # top center
        [1, -1],  # top right
        [-1, 1],  # bottom left
        [0, 1],  # bottom center
        [1, 1],  # bottom right
    ]
    for direction in directions:
        posx = row + direction[0]
        posy = col + direction[1]

        # print("check posx,posy:", posx, posy)
        if posx < 0:
            # print("first row, skip row -1")
            continue
        if posy < 0:
            # print("first col, skip col -1")
            continue

        try:
            adjacent = matrix[posy][posx]
            if adjacent == "." or adjacent.isnumeric():
                pass
            else:
                has_adjacent = True
            # print("adjacent:", adjacent)
        except IndexError:
            # print("index error for:", direction)
            pass
    return has_adjacent


def get_numbers_with_adjacents(matrix):
    numbers_with_adjacents = []
    numbers_without_adjacents = []
    for row in range(0, len(matrix)):
        current_num = ""
        current_num_has_adjacent = False
        for col in range(0, len(matrix[0])):
            cell = matrix[row][col]
            if cell.isnumeric() is False:
                if current_num != "":
                    if current_num_has_adjacent:
                        # print("✅:", current_num, "position:", row, col)
                        numbers_with_adjacents.append(int(current_num))
                    else:
                        # print("🚫:", current_num, "position:", row, col)
                        numbers_without_adjacents.append(int(current_num))
                    current_num = ""
                    current_num_has_adjacent = False
                continue
            current_num = current_num + cell
            has_adjacent = has_adjacent_symbol(row, col, matrix)
            # print(cell, "current_num", current_num, has_adjacent)
            if has_adjacent:
                current_num_has_adjacent = True
            # print("current_num:", current_num, "has_adjacent:", current_num_has_adjacent, "row,col", row,col)

        # TODO: this is only just for checking nums at the end of rows. Kinda duplication, optimize
        if current_num != "":
            if current_num_has_adjacent:
                # print("✅:", current_num)
                numbers_with_adjacents.append(int(current_num))
            else:
                # print("🚫:", current_num)
                numbers_without_adjacents.append(int(current_num))
            current_num = ""
            current_num_has_adjacent = False

    # print("numbers_with_adjacents", numbers_with_adjacents)
    # print("numbers_without_adjacents", numbers_without_adjacents)
    return numbers_with_adjacents, numbers_without_adjacents


def solve_part1(matrix):
    (numbers_with_adjacents, numbers_without_adjacents) = get_numbers_with_adjacents(
        matrix
    )
    print(sum(numbers_with_adjacents))

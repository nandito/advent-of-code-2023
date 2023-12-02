from io import TextIOWrapper

max_cube_counts = {"red": 12, "green": 13, "blue": 14}


def check_possibility(line):
    is_possible = True
    game_id = line.split(":")[0].split(" ")[1]
    sessions = line.split(":")[1].strip().split("; ")
    for session in sessions:
        rounds = session.split(", ")
        for round in rounds:
            count, color = round.split(" ")
            if max_cube_counts[color] < int(count):
                is_possible = False
                # TODO: early return

    return game_id, is_possible


def solve_part1(file: TextIOWrapper):
    """
    Solve part 1 of the puzzle.
    :param file: opened file
    :return: None
    """
    possible_game_ids = []

    for file_line in file:
        game_id, is_possible = check_possibility(file_line)
        if is_possible:
            possible_game_ids.append(int(game_id))

    print(sum(possible_game_ids))

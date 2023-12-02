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


with open("input") as f:
    lines = f.readlines()
    possible_game_ids = []

    for line in lines:
        game_id, is_possible = check_possibility(line)
        if is_possible:
            possible_game_ids.append(int(game_id))


    print(sum(possible_game_ids))

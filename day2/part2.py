import pandas as pd
from io import TextIOWrapper


def count_colors(line):
    # print("\n\nLINE:", line)
    sessions = line.split(": ")[1].strip().split("; ")
    games = pd.DataFrame(columns=["red", "green", "blue"])
    for session in sessions:
        rounds = session.split(", ")
        round_df = pd.Series(rounds, dtype="string").str.split(" ", expand=True)
        # Convert string counts to int
        round_df[0] = round_df[0].astype("int")
        # Transpose table
        round_df = round_df.T
        # Set the color as column name
        round_df.columns = round_df.iloc[1]
        # Remove the color row
        round_df = round_df[:1]
        # Add it to the games df
        games = pd.concat([round_df, games])

    # print("max:\n", games.max().prod())
    return games.max().prod()


def solve_part2(file: TextIOWrapper):
    """
    Solve part 1 of the puzzle.
    :param file: opened file
    :return: None
    """
    cube_products = []

    for file_line in file:
        cube_products.append(count_colors(file_line))

    print(sum(cube_products))

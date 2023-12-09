import numpy as np


def get_prediction(history, preds=[], round=0):
    # print(f"\nhistory: {history}, preds: {preds}, round: {round}")
    if np.all(history == 0):
        return sum(preds)
    else:
        history_diff = np.diff(history)
        # print(f"history_diff: {history_diff}, next_preds: {next_preds}")
        return get_prediction(history_diff, [*preds, history[-1]], round + 1)


def solve_part1(lines):
    values = np.array([list(map(int, line)) for line in map(str.split, lines)])
    next_values = np.array([get_prediction(row) for row in values])
    print("Sum of all predictions:", sum(next_values))

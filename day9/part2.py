import numpy as np


def rolling_diff(values):
    result = [0]
    for i in range(len(values) - 1):
        result.append(values[i] - result[i])

    return result


def get_predictor(history, preds=[], round=0):
    # print(f"\nhistory: {history}, preds: {preds}, round: {round}")
    if np.all(history == 0):
        return rolling_diff(preds)[-1]
    else:
        history_diff = np.diff(history)
        # print(f"history_diff: {history_diff}, next_preds: {next_preds}")
        return get_predictor(history_diff, [history[0], *preds], round + 1)


def solve_part2(lines):
    values = np.array([list(map(int, line)) for line in map(str.split, lines)])
    next_values = np.array([row[0] - get_predictor(row) for row in values])
    print("Sum of all -1st predictions:", sum(next_values))

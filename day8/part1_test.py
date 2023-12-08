import pandas as pd

from part1 import walk


def test_walk():
    node_map = pd.DataFrame(columns=["node", "L", "R"])
    node_map.loc[0] = ["AAA", "BBB", "CCC"]
    node_map.loc[1] = ["BBB", "DDD", "EEE"]
    node_map.loc[2] = ["CCC", "ZZZ", "GGG"]
    node_map.loc[3] = ["DDD", "DDD", "DDD"]
    node_map.loc[4] = ["EEE", "EEE", "EEE"]
    node_map.loc[5] = ["GGG", "GGG", "GGG"]
    node_map.loc[6] = ["ZZZ", "ZZZ", "ZZZ"]
    node_map.set_index("node", inplace=True)

    assert walk(node_map, "AAA", "R") == "CCC"
    assert walk(node_map, "AAA", "L") == "BBB"
    assert walk(node_map, "CCC", "R") == "GGG"

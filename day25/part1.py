import networkx as nx


def solve_part1(lines):
    G = nx.Graph()

    for line in lines:
        comps = line.strip().split(":")
        for comp in comps[1].strip().split(" "):
            # print(f"Add edge: {comps[0]}: { comp }")
            G.add_edge(comps[0], comp)

    # print(G)

    cut_value, partition = nx.stoer_wagner(G)
    # print(cut_value, partition)
    if cut_value != 3:
        raise Exception("Not 3 cuts")

    return len(partition[0]) * len(partition[1])

import re

import numpy as np


def workflow_walk(rating, entry, workflows):
    current_wf = workflows[entry]
    output = None
    fallback = None
    for condition in current_wf:
        if type(condition) is tuple:
            category, operator, size, target = condition
            for r in rating:
                # print(f"r[0]: {r[0]}, category: {category}, r[1]: {r[1]}, int(size): {int(size)}")
                if r[0] == category:
                    if operator == "<":
                        if r[1] < int(size):
                            output = target
                            break
                    elif operator == ">":
                        if r[1] > int(size):
                            output = target
                            break
                    else:
                        print(f"Unknown operator: {operator}")
            if output is not None:
                break
        else:
            fallback = condition

    return output or fallback


def parse_workflow_steps(wf):
    s = re.search(r"(\w+)([<>])(\d+):(\w+)", wf)
    steps = None
    try:
        steps = s.groups()
    except AttributeError:
        steps = wf

    return steps


def solve_part1(lines):
    workflows = {}
    ratings = []
    for line in lines:
        if line.startswith("{"):
            rating = re.sub(r"[{}]", "", line.strip()).split(",")
            rating = list(
                map(lambda x: (x.split("=")[0], int(x.split("=")[1])), rating)
            )
            ratings.append(rating)
        elif re.match(r"\w+{", line.strip()):
            workflow_name, workflow_steps = line.strip().split("{")
            workflow_steps = list(
                map(
                    parse_workflow_steps,
                    workflow_steps.split("}")[0].split(","),
                )
            )
            workflows[workflow_name] = workflow_steps

    # print("workflows", workflows)
    # print("ratings", ratings)

    accepted = []

    for rating in ratings:
        steps = []
        entry = "in"
        while True:
            steps.append(entry)
            if entry == "A":
                accepted.append(rating)
            if entry == "A" or entry == "R":
                break
            entry = workflow_walk(rating, entry, workflows)

    return np.sum(np.sum(np.array(accepted)[:, :, 1].astype(int), axis=1))

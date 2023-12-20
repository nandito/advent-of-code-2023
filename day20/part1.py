import re



def solve_part1(lines):
    module_configuration = []
    graph = {}
    for line in lines:
        line_parts = line.strip().split(" -> ")
        name = line_parts[0]
        name_type = re.search(r"([%&])", name)
        if name_type:
            name_type = name_type.group(1)
            name = name.replace(name_type, "")
        else:
            name_type = "broadcaster"
        destinations = line_parts[1].split(", ")
        graph[name] = destinations
        module_configuration.append((name, "low", name_type, destinations))

    print(module_configuration)
    return 0

from math import ceil, log10


def apply_maps(maps, seed):
    pre_map = seed
    for m in maps:
        for ds, ss, rl in m:
            if ss <= pre_map < ss + rl:
                pre_map = ds + (pre_map - ss)
                break
    return pre_map


def parse_input(lines):
    seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]
    seeds = [(seeds[2 * i], seeds[2 * i + 1]) for i in range(len(seeds) // 2)]

    maps = []
    curr_map = []
    for line in lines[3:]:
        if line == "":
            continue
        if ":" in line:
            maps += [curr_map]
            curr_map = []
        else:
            curr_map += [tuple(int(x) for x in line.split(" "))]

    maps += [curr_map]

    return seeds, maps


def solve_part2(lines):
    lines = [line.strip() for line in lines]

    seeds, maps = parse_input(lines)

    step_size = int(pow(10, ceil(log10(max(s[1] for s in seeds) / 100))))
    search_vals = {
        (ss, ss + sl, s): apply_maps(maps, s)
        for ss, sl in seeds
        for s in range(ss, ss + sl, step_size)
    }
    rough_est = min(search_vals.items(), key=lambda x: x[1])

    seed_range_start, seed_range_end, best_est = rough_est[0]
    print(
        f"Best estimate: {best_est} in seed range {seed_range_start} to {seed_range_end}"
    )
    print(
        f"Step size: {step_size:<8d}, best estimate: {best_est:<10d} near loc {rough_est[1]}"
    )

    best_loc = rough_est[1]

    while step_size > 1:
        left_search = max(best_est - step_size, seed_range_start)
        right_search = min(best_est + step_size, seed_range_end)

        step_size = step_size // 10
        search_vals = {
            s: apply_maps(maps, s) for s in range(left_search, right_search, step_size)
        }
        best_est, best_loc = min(search_vals.items(), key=lambda x: x[1])

        print(
            f"Step size: {step_size:<8d}, best estimate: {best_est:<10d} near loc {best_loc}"
        )

    return best_loc

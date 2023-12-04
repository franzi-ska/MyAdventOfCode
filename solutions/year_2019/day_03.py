def wires(input_str: str, mode: str):
    move = {
        'R': [1, 0],
        'U': [0, 1],
        'L': [-1, 0],
        'D': [0, -1]
    }

    positions = {0: [], 1: []}
    for index, wire in enumerate(input_str.splitlines()):
        p = [0, 0]
        for instruction in wire.split(','):
            direction = instruction[0]
            n_step = int(instruction[1:])
            for n in range(n_step):
                p = [x+y for x, y in zip(p, move[direction])]
                positions[index].append(tuple(p))

    intersections = set(positions[0]) & set(positions[1])

    if mode == "a":
        manhattan_d = [sum([abs(i) for i in item]) for item in intersections]
        return min(manhattan_d)
    elif mode == "b":
        run_times = [sum([positions[w].index(i) for w in [0, 1]]) for i in intersections]
        return min(run_times) + 2  # +2 for the two initial steps


def part_a(input_str: str):
    mode = "a"
    return wires(input_str, mode)


def part_b(input_str: str):
    mode = "b"
    return wires(input_str, mode)

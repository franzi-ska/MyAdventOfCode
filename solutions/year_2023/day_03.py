import re


def get_positions(s: str, regex):
    positions = {}
    idx = 0
    for row, line in enumerate(s.splitlines()):
        for match in regex.finditer(line):
            idx += 1
            [col0, col1] = match.span()
            positions[idx] = {'value': match.group(0),
                              'position':  [(row, c) for c in range(col0, col1)]
                              }
    return positions


def get_surrounding(position: tuple):
    surrounding = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if not dx == dy == 0:
                surrounding.append((position[0] - dx, position[1] - dy))
    return surrounding


def part_a(input_str: str):
    number_regex = re.compile('\d+')
    symbol_regex = re.compile('[^\d.\s]')

    numbers = get_positions(input_str, number_regex)
    symbols = get_positions(input_str, symbol_regex)

    symbol_surrounding = {s: get_surrounding(p['position'][0]) for s, p in symbols.items()}

    sum_of_parts = 0
    for n_idx, number in numbers.items():
        for symbol_idx, surrounding in symbol_surrounding.items():
            if set(number["position"]) & set(surrounding):
                sum_of_parts += int(number["value"])
                break
    return sum_of_parts


def part_b(input_str: str):
    number_regex = re.compile('\d+')
    symbol_regex = re.compile('[^\d.\s]')

    numbers = get_positions(input_str, number_regex)
    symbols = get_positions(input_str, symbol_regex)

    symbol_surrounding = {s: get_surrounding(p['position'][0]) for s, p in symbols.items()}

    gear_ratio_sum = 0
    for s_idx, symbol in symbols.items():
        if not symbol["value"] == "*":
            continue
        numbers_in_surrounding = []
        for number in numbers.values():
            if set(number["position"]) & set(symbol_surrounding[s_idx]):
                numbers_in_surrounding.append(int(number["value"]))

            if len(numbers_in_surrounding) > 2:
                break
        if len(numbers_in_surrounding) == 2:
            gear_ratio_sum += numbers_in_surrounding[0] * numbers_in_surrounding[1]

    return gear_ratio_sum

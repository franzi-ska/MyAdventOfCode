import math
import re

re_maps = re.compile(r"\b(\w+)-to-(\w+) map:\n(([\d \n]+\d)+)")
re_seeds = re.compile(r"seeds: ([\d ]+)")


class Map:
    def __init__(self, s: str, reverse: bool):
        self.c = []
        for line in s.splitlines():
            if reverse:
                idx0, jdx0, r = [int(i) for i in line.split()]
            else:
                jdx0, idx0, r = [int(i) for i in line.split()]
            self.c.append((range(idx0, idx0+r), jdx0-idx0))

    def map(self, i: int) -> int:
        for m in self.c:
            if i in m[0]:
                return i + m[1]
        return i


def get_match_dict(input_str, reverse=False):
    match_dict = {}
    matches = re_maps.findall(input_str)
    if reverse:
        matches.reverse()
    for match in matches:
        # print(match)
        key = f"{match[0]}2{match[1]}"
        match_dict[key] = Map(match[2], reverse)

    return match_dict


def part_a(input_str: str):
    match_dict = get_match_dict(input_str)
    seeds = [int(i) for i in re_seeds.match(input_str)[1].split()]
    position_min = math.inf
    for value in seeds:
        for step, converter in match_dict.items():
            value = converter.map(value)

        position_min = min(position_min, value)
    return position_min


def part_b(input_str: str):
    match_dict = get_match_dict(input_str, reverse=True)
    seeds = [int(i) for i in re_seeds.match(input_str)[1].split()]

    n_pairs = len(seeds)//2

    seed_ranges = []
    for p in range(n_pairs):
        seed0 = seeds.pop(0)
        seed_range = seeds.pop(0)
        seed_ranges.append(range(seed0, seed0+seed_range))

    max_position = part_a(input_str)
    position = -1
    while True:
        try :
            position += 1

            if position % 1000000 == 0:
                print(position, f'min {int(position / max_position *100)}%')
            value = position * 1
            for step, converter in match_dict.items():
                value = converter.map(value)

            if any([value in seed_range for seed_range in seed_ranges]):
                break
        except KeyboardInterrupt:
            print(f'Interrupted: Last tested: {position-1}')
            position = None
            break

    return position


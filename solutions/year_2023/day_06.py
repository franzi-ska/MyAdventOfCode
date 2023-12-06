import math
import re


def parse_input(input_str: str):
    lines = input_str.splitlines()
    numbers = re.compile("\d+")
    times = numbers.findall(lines[0])
    distances = numbers.findall(lines[1])
    pairs = [(int(t), int(d)) for t,d in zip(times, distances)]
    return pairs


def solve_race(time, distance):
    # press^2 - time * press + distance = =
    press_min = math.ceil(- -time/2 - ((-time/2)**2 - distance)**(1/2))
    press_max = math.floor(- -time/2 + ((time/2)**2 - distance)**(1/2))
    n_options = press_max - press_min + 1
    return n_options


def part_a(input_str: str):
    races = parse_input(input_str)
    return math.prod([solve_race(*race) for race in races])


def part_b(input_str: str):
    race = parse_input(input_str.replace(' ', ''))
    return solve_race(*race[0])

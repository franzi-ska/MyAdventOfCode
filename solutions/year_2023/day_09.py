from typing import List

import numpy as np


def line_to_ints(s: str) -> List[int]:
    return [int(i) for i in s.split()]


def part_a(input_str: str):
    result = 0
    for line in input_str.splitlines():
        last_elements = []
        array = np.array(line_to_ints(line))
        while np.any(array):
            last_elements.append(array[-1] * 1)
            array = np.diff(array)
        result += sum(last_elements)
    return result


def part_b(input_str: str):
    result = 0
    for line in input_str.splitlines():
        first_element = []
        array = np.array(line_to_ints(line))
        while np.any(array):
            first_element.append(array[0] * 1)
            array = np.diff(array)

        new_item = 0
        for item in first_element[::-1]:
            new_item = item - new_item

        result += new_item
    return result

import itertools
import math
import re


def parse_input(input_str: str):
    re_line = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    lines = input_str.splitlines()
    instructions = lines.pop(0)
    instructions = [1 if i == 'R' else 0 for i in instructions]
    out = {}
    for line in lines[1:]:
        match = re_line.match(line)
        out[match[1]] = [match[2], match[3]]
    return out, instructions


def to_dst_node(start_node, nodes, instructions, dst_node: str = False):
    this_node = start_node
    count = None
    for count, direction in enumerate(itertools.cycle(instructions)):
        this_node = nodes[this_node][direction]
        if dst_node and dst_node == this_node:
            break
        elif not dst_node and this_node.endswith("Z"):
            break
    return count + 1


def part_a(input_str: str):
    nodes, instructions = parse_input(input_str)
    return to_dst_node("AAA", nodes, instructions, dst_node="ZZZ")


def part_b(input_str: str):
    nodes, instructions = parse_input(input_str)
    dst_nodes = [to_dst_node(key, nodes, instructions) for key in nodes.keys() if key.endswith("A")]
    return math.lcm(*dst_nodes)


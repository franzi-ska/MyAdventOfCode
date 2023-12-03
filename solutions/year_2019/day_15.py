from collections import deque

from solutions.year_2019.intcode_computer import IntcodeComputer


class RepairDroid:
    def __init__(self, code):
        self.brain = IntcodeComputer(code, pause_on_output=True)
        self.path = []
        self.position = [0, 0]
        self.next_move = deque([1, 3, 2, 4])
        self.oxygen_source = None

    def run_direct_to_oxygen(self):
        output_value = None
        while not output_value == 2:
            move = self.next_move[0]
            self.brain.set_input(move)
            output_value = self.brain.run()
            if output_value:  # robot moved
                self.update_position(move)
                self.check_backtracking()
            self.decide_next_move(output_value > 0)

    def map_dungeon(self):
        while True:
            move = self.next_move[0]
            self.brain.set_input(move)
            output_value = self.brain.run()
            if output_value:  # robot moved
                self.update_position(move)
                if output_value == 2:
                    self.oxygen_source = self.position * 1

            self.decide_next_move(output_value > 0)
            self.path.append(tuple(self.position) * 1)
            if output_value > 0 and self.path[-1] == (0, 0):
                break

    def update_position(self, move):
        if move == 1:  # north
            self.position[0] += 1
        elif move == 2:  # south
            self.position[0] -= 1
        elif move == 3:  # west
            self.position[1] += 1
        elif move == 4:  # east
            self.position[1] -= 1

    def check_backtracking(self):
        new_position = self.position
        if self.position in self.path:
            idx = self.path.index(self.position)

            self.path = self.path[0:idx + 1]
        else:
            self.path.append(self.position * 1)

    def decide_next_move(self, did_move):
        if did_move:
            self.next_move.rotate(1)
        else:
            self.next_move.rotate(-1)


def where_next(options, front):
    new_front = []
    for item in front:
        surrounding = [(item[0] - 1, item[1]),
                       (item[0] + 1, item[1]),
                       (item[0], item[1] + 1),
                       (item[0], item[1] - 1)]
        overlap = set(surrounding) & set(options)
        if overlap:
            new_front.extend(list(overlap))
    return list(set(new_front))


def part_a(input_str: str):
    intcode = [int(c) for c in input_str.split(',')]
    droid = RepairDroid(intcode)
    droid.run_direct_to_oxygen()
    return len(droid.path)


def part_b(input_str: str):
    intcode = [int(c) for c in input_str.split(',')]
    droid = RepairDroid(intcode)
    droid.map_dungeon()
    no_oxygen = list(set(droid.path))
    no_oxygen.remove(tuple(droid.oxygen_source))
    new_oxygen = [tuple(droid.oxygen_source)]

    count = 0
    while no_oxygen:
        count += 1
        new_oxygen = where_next(no_oxygen, new_oxygen)

        for ox in new_oxygen:
            no_oxygen.remove(ox)

    return count

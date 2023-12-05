from collections import defaultdict, deque

from solutions.year_2019.intcode_computer import IntcodeComputer


class HullPaintingRobot:
    def __init__(self, code):
        self.brain = IntcodeComputer(code, pause_on_output=True)
        self.position = [0, 0]
        self.direction = deque(['down', 'left', 'up', 'right',])
        self.grid_state = defaultdict(lambda: 0)

    def move(self):
        # use camera to get current color
        camera_color = self.grid_state[tuple(self.position)]
        self.brain.set_input(camera_color)

        # paint current position according to brain
        color_to_paint = self.brain.run()
        self.grid_state[tuple(self.position)] = color_to_paint

        # where to turn?
        turn_direction = self.brain.run()
        rotate_by = 1 if turn_direction == 1 else -1
        self.direction.rotate(rotate_by)

        # move to next square
        facing = self.direction[0]
        if facing == "up":
            self.position[1] += 1
        elif facing == "down":
            self.position[1] -= 1
        elif facing == "right":
            self.position[0] += 1
        elif facing == "left":
            self.position[0] -= 1


def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    robot = HullPaintingRobot(code)
    while not robot.brain.program_finished:
        robot.move()
    grid = dict(robot.grid_state)
    n_grid = len(grid)
    return n_grid


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    robot = HullPaintingRobot(code)
    robot.grid_state[(0, 0)] = 1
    while not robot.brain.program_finished:
        robot.move()
    grid = dict(robot.grid_state)

    positions = grid.keys()
    offsets = [0, 0]
    max_pos = [0, 0]
    for idx in range(2):
        pos = [p[idx] for p in positions]
        max_pos[idx] = max(pos)

    hull = [[' ' for i in range(max_pos[0] + 1)] for j in range(max_pos[1]+ 1)]

    for pos, paint in grid.items():
        hull[pos[1]-offsets[1]][pos[0]-offsets[0]] = 'X' if paint == 1 else ' '

    output = '\n'.join([''.join(line) for line in hull])
    return '\n' + output


if __name__ == '__main__':
    # For debugging
    pass

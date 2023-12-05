import time

import matplotlib.pyplot as plt

from solutions.year_2019.intcode_computer import IntcodeComputer


class ArcadeCabinet:
    def __init__(self, code):
        self.brain = IntcodeComputer(code, pause_on_output=True)
        self.screen = dict()
        self.color_dict = {
            0: None,  # empty
            1: "black",  # wall
            2: "orange",  # block
            3: "brown",  # horizontal_paddle
            4: "blue",  # ball
        }
        self.x_ball = None
        self.x_paddle = None
        self.score = 0

    def run(self):
        while not self.brain.program_finished:
            if self.brain.wait_for_input:
                move = self.decide_next_move()
                self.brain.set_input(move)
            x = self.brain.run()
            y = self.brain.run()

            if (x == -1) and (y == 0):
                self.score = self.brain.run()
            else:
                tile_id = self.brain.run()
                if tile_id == 4:
                    self.x_ball = x * 1
                elif tile_id == 3:
                    self.x_paddle = x * 1
                self.screen[(x, y)] = tile_id

    def show_screen(self, ax=None):
        if not ax:
            fig, ax = plt.subplots(1, 1, figsize=(10, 5))
            ax.invert_yaxis()
            ax.axis("equal")

        for position, item_id in self.screen.items():
            if item_id:
                ax.plot(*position, 's', color=self.color_dict[item_id], markersize=10)
        ax.set_title(f"Score: {self.score}")
        plt.show()

    def decide_next_move(self):
        if self.x_ball == self.x_paddle:
            move = 0
        elif self.x_ball < self.x_paddle:
            move = -1
        else:
            move = 1
        return move


# correct solution : 280
def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    arcade = ArcadeCabinet(code)
    arcade.run()
    n_blocks = sum([1 for value in arcade.screen.values() if value == 2])
    arcade.show_screen()
    return n_blocks


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    arcade = ArcadeCabinet(code)
    arcade.brain.set_value(0, 2)
    arcade.run()
    return arcade.score


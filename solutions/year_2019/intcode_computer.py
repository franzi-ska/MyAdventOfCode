from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Instruction:
    method: Callable
    n_args: int

    def __post_init__(self):
        self.n = self.n_args + 1


class IntcodeComputer:
    def __init__(self, intcode: List[int], debug=False):
        self.memory = intcode
        self.pointer = 0
        self.program_finished = False
        self.input_list = []
        self.next_input = 0
        self.output_list = []

        self.debug = debug

        self._instructions = {
            1: Instruction(self._operation_add, 3),
            2: Instruction(self._operation_multiply, 3),
            3: Instruction(self._operation_input, 1),
            4: Instruction(self._operation_output, 1),
            5: Instruction(self._operation_jump_if_true, 2),
            6: Instruction(self._operation_jump_if_false, 2),
            7: Instruction(self._operation_less_than, 3),
            8: Instruction(self._operation_equals, 3),
            99: Instruction(self._operation_halt, 0)
        }

    def __str__(self):
        st = ''
        for p in ["memory", "pointer", "input_list", "output_list"]:
            st += f'{p}:\t{getattr(self, p)}\n'
        return st

    def run(self):
        count = 0
        while not self.program_finished:
            instruction = self.memory[self.pointer]
            opcode, modes = self.decode_instruction(instruction)

            if self.debug:
                print('\n', 'Clock', count)
                print(self)

            operation = self._instructions[opcode]

            if operation.n_args > 0:
                args = self.memory[self.pointer+1: self.pointer+operation.n]
                operation.method(args, modes)
            else:
                operation.method()

            count +=1

    def set_value(self, position, value):
        self.memory[position] = value

    def get_value(self, position):
        return self.memory[position]

    def move_pointer(self, move_by):
        self.pointer += move_by

    def set_input(self, value):
        self.input_list.append(value)

    def decode_instruction(self, instruction):
        opcode = instruction % 100
        parameter_modes = str(instruction)[:-2]
        n_args = self._instructions[opcode].n_args
        if len(parameter_modes) < n_args:
            parameter_modes = '0' * (n_args - len(parameter_modes)) + parameter_modes
        parameter_modes = [int(c) for c in parameter_modes[::-1]]
        return opcode, parameter_modes

    def get_immediate_value(self, value_in, mode):
        if mode:
            # immediate mode (mode == 1)
            value_out = value_in
        else:
            # position mode (mode == 0)
            value_out = self.memory[value_in]
        return value_out

    def _operation_add(self, args, modes):
        src0, src1, dst = args
        src0 = self.get_immediate_value(src0, modes[0])
        src1 = self.get_immediate_value(src1, modes[1])
        self.set_value(dst, src0 + src1)
        self.move_pointer(4)

    def _operation_multiply(self, args, modes):
        src0, src1, dst = args
        src0 = self.get_immediate_value(src0, modes[0])
        src1 = self.get_immediate_value(src1, modes[1])
        self.set_value(dst, src0 * src1)
        self.move_pointer(4)

    def _operation_input(self, args, modes):
        current_input = self.input_list[self.next_input]
        dst = args[0]
        self.set_value(dst, current_input)
        self.next_input += 1
        self.move_pointer(2)

    def _operation_output(self, args, modes):
        src = self.get_immediate_value(args[0], modes[0])
        self.output_list.append(src)
        self.move_pointer(2)
        if self.debug:
            print('Current output: ', self.output_list)

    def _operation_jump_if_true(self, args, modes):
        to_test = self.get_immediate_value(args[0], modes[0])
        if not (to_test == 0):
            value = self.get_immediate_value(args[1], modes[1])
            self.pointer = value
        else:
            self.move_pointer(3)

    def _operation_jump_if_false(self, args, modes):
        to_test = self.get_immediate_value(args[0], modes[0])
        if to_test == 0:
            value = self.get_immediate_value(args[1], modes[1])
            self.pointer = value
        else:
            self.move_pointer(3)

    def _operation_less_than(self, args, modes):
        value0 = self.get_immediate_value(args[0], modes[0])
        value1 = self.get_immediate_value(args[1], modes[1])
        dst = args[2]
        self.set_value(dst, int(value0 < value1))
        self.move_pointer(4)

    def _operation_equals(self, args, modes):
        value0 = self.get_immediate_value(args[0], modes[0])
        value1 = self.get_immediate_value(args[1], modes[1])
        dst = args[2]
        self.move_pointer(4)

        self.set_value(dst, int(value0 == value1))

    def _operation_halt(self):
        self.program_finished = True
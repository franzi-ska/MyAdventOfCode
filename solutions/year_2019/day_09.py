from solutions.year_2019.intcode_computer import IntcodeComputer


def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    ic = IntcodeComputer(code)
    ic.set_input(1)
    ic.run()
    print(ic.output_list)
    return ic.output_list[-1]


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    ic = IntcodeComputer(code)
    ic.set_input(2)
    ic.run()
    print(ic.output_list)
    return ic.output_list[-1]


if __name__ == '__main__':
    # For debugging
    pass

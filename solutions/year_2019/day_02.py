from solutions.year_2019.intcode_computer import IntcodeComputer


def part_a(input_str: str):
    intcode = [int(i) for i in input_str.split(',')]
    computer = IntcodeComputer(intcode)
    computer.set_value(1, 12)
    computer.set_value(2, 2)

    computer.run()
    return computer.get_value(0)


def part_b(input_str: str):
    intcode = [int(i) for i in input_str.split(',')]
    for noun in range(91):
        for verb in range(91):
            computer = IntcodeComputer(intcode * 1)
            computer.set_value(1, noun)
            computer.set_value(2, verb)
            computer.run()
            if computer.get_value(0) == 19690720:
                return 100 * noun + verb

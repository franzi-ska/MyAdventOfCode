import itertools

from solutions.year_2019.intcode_computer import IntcodeComputer



def run_amp_chain(phase_list, amplifier_code):
    amp_input = 0
    for amp_idx, phase in zip(range(5), phase_list):
        amp = IntcodeComputer(amplifier_code)
        amp.set_input(phase)
        amp.set_input(amp_input)
        amp.run()
        amp_input = amp.output_list[-1]
    return amp_input


def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]

    max_value = 0
    for phase_list in itertools.permutations(range(5)):
        max_value = max(max_value, run_amp_chain(phase_list, code))

    return max_value


def part_b(input_str: str):
    return None


if __name__ == '__main__':
    c = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
    print(part_a(c))


import itertools

from solutions.year_2019.intcode_computer import IntcodeComputer



def run_amp_chain(phase_list, amplifier_code):
    amp_input = 0
    for amp_idx, phase in zip(range(5), phase_list):
        amp = IntcodeComputer(amplifier_code, pause_on_output=True)
        amp.set_input(phase)
        amp.set_input(amp_input)
        amp.run()
        amp_input = amp.output_list[-1]
    return amp_input

def run_feedback_loop(phase_list, amplifier_code):
    n_amps = 5
    amps = []
    # initilize amps
    for idx, phase in enumerate(phase_list):
        amps.append(IntcodeComputer(amplifier_code, pause_on_output=True))
        amps[idx].set_input(phase)
    # provide initial input

    last_output = 0

    for current_amp in itertools.cycle(amps):
        current_amp.set_input(last_output)
        current_amp.run()
        last_output = current_amp.output_list[-1]
        if current_amp.program_finished:
            break

    return amps[-1].output_list[-1]


def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]

    max_value = 0
    for phase_list in itertools.permutations(range(5)):
        max_value = max(max_value, run_amp_chain(phase_list, code))

    return max_value


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    max_value = 0
    for phase_list in itertools.permutations(range(5, 10)):
        max_value = max(max_value, run_feedback_loop(phase_list, code))
    return max_value


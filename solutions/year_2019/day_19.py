from solutions.year_2019.intcode_computer import IntcodeComputer


def test_input(code, x, y):
    ic = IntcodeComputer(code, pause_on_output=True)
    ic.set_input(x)
    ic.set_input(y)
    output = ic.run()
    return output


def part_a(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    n = 50
    count = 0
    start_search = 0
    for row_idx in range(0, n):
        start_updated = False
        for col_idx in range(start_search, n):

            status = test_input(code, col_idx, row_idx)
            count += status
            if (not start_updated) and status:
                start_updated = True
                start_search = col_idx

            if start_updated and not status:
                break

    return count


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    x = y = 0
    while not test_input(code, x + 99, y):
        y += 1
        while not test_input(code, x, y + 99):
            x += 1
    return x * 10000 + y

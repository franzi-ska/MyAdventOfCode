from solutions.year_2019.intcode_computer import IntcodeComputer


def get_scaffold_image(code_str):
    code = [int(i) for i in code_str.split(',')]
    ic = IntcodeComputer(code)
    ic.run()

    ascii_output = ''.join([chr(i) for i in ic.output_list])
    return ascii_output


def get_alignment(image: str):
    row_list = image.splitlines()
    n_row = len(row_list)
    n_col = len(row_list[0])
    alignment_parameter = 0
    for row_idx, row in enumerate(row_list):
        if 0 < row_idx < n_row - 2:

            for col_idx, c in enumerate(row):
                if 0 < col_idx < n_col - 2:
                    if c == '#':
                        if row_list[row_idx-1][col_idx] == row_list[row_idx+1][col_idx] \
                                == row_list[row_idx][col_idx-1] == row_list[row_idx][col_idx+1]\
                                == '#':
                            alignment_parameter += row_idx * col_idx
                            # print(f"{row_idx}/{n_row}\t{col_idx}/{n_col}")

    return alignment_parameter


def part_a(input_str: str):
    if input_str[0].isdigit():
        scaffold_image = get_scaffold_image(input_str)
    else:
        scaffold_image = input_str  # test case

    print(scaffold_image)
    # with open('scaffold_image.txt', 'w') as f:
    #     f.write(scaffold_image)

    alignment_value = get_alignment(scaffold_image)
    return alignment_value


def part_b(input_str: str):
    code = [int(i) for i in input_str.split(',')]
    ic = IntcodeComputer(code)

    # wake up the vacuum robot
    ic.set_value(0, 2)

    # hard coded solution for my input, solved on paper
    # Steps:
    #   - found path over scaffold
    #   - split into 3 repeated block
    main_movement = 'A,B,A,B,C,A,C,A,C,B'
    movement_a = 'R,12,L,8,L,4,L,4'
    movement_b = 'L,8,R,6,L,6'
    movement_c = 'L,8,L,4,R,12,L,6,L,4'

    for instruction in [main_movement, movement_a, movement_b, movement_c]:
        for c in instruction:
            ic.set_input(ord(c))
        ic.set_input(ord('\n'))

    ic.set_input(ord('n'))
    ic.set_input(ord('\n'))

    ic.run()

    return ic.output_list[-1]

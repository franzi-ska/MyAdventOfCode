import re

n_row = 6
n_col = 25
re_layer = re.compile('\d{150}')


def part_a(input_str: str):
    layer_list = re_layer.findall(input_str)
    n_zeros = [sum(c == "0" for c in layer) for layer in layer_list]
    min_zero = min(n_zeros)
    print(n_zeros)
    idx = [i for i, item in enumerate(n_zeros) if item == min_zero][0]
    n_one = sum(c == "1" for c in layer_list[idx])
    n_two = sum(c == "2" for c in layer_list[idx])
    return n_one * n_two


def part_b(input_str: str):
    layer_list = re_layer.findall(input_str)
    layer_list.reverse()

    image = [[' ' for c in range(n_col)] for r in range(n_row)]
    for layer in layer_list:
        for idx, c in enumerate(layer):
            col_idx = idx % n_col
            row_idx = idx // n_col
            if c == "0":  # black
                image[row_idx][col_idx] = ' '
            elif c == "1":  # white
                image[row_idx][col_idx] = "#"
            else:
                pass  # transparent

    img = '\n' + '\n'.join([''.join([c for c in row]) for row in image])
    return img

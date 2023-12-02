import re


def part_a(input_str: str):

    count = 0

    for game in input_str.splitlines():

        valid_game = True

        game_name, games = game.split(':')
        game_idx = int(game_name.split(' ')[1])
        pull_list = games.split(";")
        for pull in pull_list:
            color_list = pull.split(',')
            for color in color_list:
                n_color, name_color = color.strip().split(' ')

                if name_color == "red" and int(n_color) > 12:
                    valid_game = False
                if name_color == "green" and int(n_color) > 13:
                    valid_game = False
                if name_color == "blue" and int(n_color) > 14:
                    valid_game = False

        if valid_game:
            count += int(game_idx)

    return count


def part_b(input_str: str):
    count = 0
    regexs = {"red": re.compile("(\d+) red"),
              "green": re.compile("(\d+) green"),
              "blue": re.compile("(\d+) blue")
              }

    for idx, game in enumerate(input_str.splitlines()):
        p = 1
        for color, r in regexs.items():
            n_col = max([int(i) for i in r.findall(game)])
            p *= n_col
        count += p
    return count

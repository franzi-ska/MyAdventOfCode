import sys

from utils_aoc.aoc_day import AocDay


if __name__ == '__main__':

    run_mode = sys.argv[1]

    n_args = len(sys.argv) - 2
    if n_args == 2:
        year = sys.argv[2]
        day = sys.argv[3]
    elif n_args == 1:
        day = sys.argv[2]
        year = None



    else:
        day, year = None, None

    aoc_day = AocDay(year=year, day=day)

    if run_mode == "setup":
        aoc_day.create_folders_and_files()
        aoc_day.download_input_from_website()

    elif run_mode == "test":
        aoc_day.run_tests()

    elif run_mode == "run":
        aoc_day.run_input()


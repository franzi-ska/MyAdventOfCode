import importlib
import os
import re
import shutil
from datetime import datetime

import requests

from utils_aoc.user_data import USER_TOKEN, USER_EMAIL, MAIN_DIR


class AocDay:
    def __init__(self, day:int = None, year= None):
        year, day = self.check_inputs(year, day)
        main_dir = os.path.join(MAIN_DIR, "solutions")

        self.year = year
        self.day = day

        self.dir_year = os.path.join(main_dir, f"year_{self.year}")
        self.dir_input = os.path.join(self.dir_year, "inputs")
        self.dir_tests = os.path.join(self.dir_year, "test_cases")

        self.file_input = os.path.join(self.dir_input, f"day_{self.day:02d}.txt")
        self.file_solution = os.path.join(self.dir_year, f"day_{self.day:02d}.py")
        self.file_test_cases = os.path.join(self.dir_tests, f"day_{self.day:02d}.txt")

        self.import_path_solution = f"solutions.year_{self.year}.day_{self.day:02}"

        self.url_puzzle = f"https://adventofcode.com/{self.year}/day/{self.day}"
        self.url_input = f"https://adventofcode.com/{self.year}/day/{self.day}/input"

        self.user_email = USER_EMAIL
        self.user_token = USER_TOKEN

        self.test_case_regex = (r"#+ TestCase (\d+) #+\n"
                                r"#+ Input #+\n"
                                r"([\S\s]*?)\n"
                                r"#+ Solution #+\n"
                                r"Part 1:(.*?)\n"
                                r"Part 2:(.*?)\n"
                                r"#+\n")

        self.template_testcase = os.path.join(MAIN_DIR, "utils_aoc\\templates\\test_case.txt")
        self.template_solution = os.path.join(MAIN_DIR, "utils_aoc\\templates\\day_solution.py")

    def create_folders_and_files(self):
        os.makedirs(self.dir_year, exist_ok=True)
        os.makedirs(self.dir_input, exist_ok=True)
        os.makedirs(self.dir_tests, exist_ok=True)

        init_file = os.path.join(self.dir_year, '__init__.py')
        if not os.path.isfile(init_file):
            with open(init_file, 'w'):
                pass

        if not os.path.isfile(self.file_test_cases):
            shutil.copyfile(src=self.template_testcase, dst=self.file_test_cases)

        if not os.path.isfile(self.file_solution):
            shutil.copyfile(src=self.template_solution, dst=self.file_solution)

    def download_input_from_website(self):
        if not os.path.isfile(self.file_input):
            r = requests.get(self.url_input,
                             cookies={'session': f'{self.user_token}'},
                             headers={"User-Agent": f"email: {self.user_email}"}
                             )
            with open(self.file_input, 'w') as f:
                f.write(r.text)

    @staticmethod
    def check_inputs(year, day):
        if not year and not day:
            year = input("What year?\t")
            day = input("What day?\t")
        elif not year and day:
            year = datetime.now().year
        year = int(year)
        day = int(day)
        return year, day

    def run_solution_function(self, input_str, part):
        funcs = importlib.import_module(self.import_path_solution, package=None)
        solution = getattr(funcs, part)(input_str)
        return str(solution)

    def run_input(self):
        with open(self.file_input) as f:
            input_str = f.read()
        output_a = self.run_solution_function(input_str, "part_a")
        output_b = self.run_solution_function(input_str, "part_b")
        print(f'Part A:\t{output_a}\nPart B:\t{output_b}')


    def run_single_test(self, part, input_str, solution, test_idx=''):
        output = self.run_solution_function(input_str, part)
        if not output == solution:
            print(f'{test_idx} {part}:\n{input_str}\n\twant:\t{solution}\n\tgot:\t{output}')
        return output == solution

    def run_tests(self):
        with open(self.file_test_cases) as f:
            test_str = f.read()
        matches = re.findall(self.test_case_regex, test_str)
        overview = [[None, None] for m in matches if m[1]]
        for jdx, [idx, input_str, solution_1, solution_2] in enumerate(matches):
            if input_str:
                if solution_1:
                    overview[jdx][0] = self.run_single_test('part_a', input_str, solution_1, test_idx=idx)
                if solution_2:
                    overview[jdx][1] = self.run_single_test('part_b', input_str, solution_2, test_idx=idx)

        if all([s[0] for s in overview]):
            print('Part A: ok')
        if all([s[1] for s in overview]):
            print('Part B: ok')

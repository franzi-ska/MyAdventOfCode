import re

re_double_digits = re.compile(r"(\d)\1+")
re_multi = re.compile(r"(\d)\1{2,}")


def increasing_numbers(s: str):
    n = [int(i) for i in s]
    for i0, i1 in zip(n, n[1:]):
        if i0 > i1:
            return 0
    return 1


def check_pwd(pwd: str, mode):
    v = 0
    if len(pwd) == 6:
        if re_double_digits.findall(pwd):
            if increasing_numbers(pwd):
                v = 1
    if v and mode == 2:
        for m in re_multi.findall(pwd):
            pwd = pwd.replace(m, '')
        if not re_double_digits.findall(pwd):
            v = 0
    return v


def count_valid(input_str, mode):
    n0, n1 = [int(i) for i in input_str.split('-')]
    n = sum([check_pwd(str(i), mode) for i in range(n0, n1+1)])
    return n


def part_a(input_str: str):
    return count_valid(input_str, 1)


def part_b(input_str: str):
    return count_valid(input_str, 2)


import re


def get_digit(s: str):
    d = 0
    for c in s:
        if c.isdigit():
            d = c
            break
    return d


def rep_text(s: str):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, d in enumerate(digits):
        s = s.replace(d, str(i+1))
    return s


def part_a(input_str: str):
    count = 0
    for line in input_str.splitlines():
        d0 = get_digit(line)
        d1 = get_digit(line[::-1])

        count += int(f'{d0}{d1}')
    return count


def part_b(input_str: str):
    digits = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|ten|\d))')

    count = 0
    for line in input_str.splitlines():
        match = digits.findall(line)
        count += int(f'{rep_text(match[0])}{rep_text(match[-1])}')
    return count

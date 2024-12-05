import os
import re
from typing import List


FILE_PATH = "input"


def main(path):
    input_string = read_file(path)

    is_enabled = True
    sum = 0

    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)", input_string)

    for match in matches:
        if "don't()" in match.group(0):
            input_string = input_string[match.end() :]
            is_enabled = False
        elif "do()" in match.group(0):
            input_string = input_string[match.end() :]
            is_enabled = True
        elif is_enabled:
            input_string = input_string[match.end() :]
            var1 = int(match.group(1))
            var2 = int(match.group(2))
            sum += var1 * var2

    print(sum)


def read_file(path: str) -> List[str]:
    with open(path) as input_file:
        lines: List[str] = []
        for line in input_file:
            lines.append(line)
        return "".join(lines)


if __name__ == "__main__":
    main(FILE_PATH)

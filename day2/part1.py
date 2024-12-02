import os
from typing import List


FILE_PATH = "input"


def main(path) -> int:
    full_path = os.path.join(os.path.dirname(__file__), path)
    number_lists = read_file(full_path)

    amount_of_safe_reports = 0
    for number_list in number_lists:
        is_increasing_list = number_list[0] < number_list[1]

        is_safe = True

        for i in range(len(number_list) - 1):
            num_1 = number_list[i]
            num_2 = number_list[i + 1]
            is_increasing = num_1 < num_2

            if is_increasing_list != is_increasing:
                is_safe = False
                break

            diff = abs(num_1 - num_2)
            if diff < 1 or diff > 3:
                is_safe = False

        if is_safe:
            amount_of_safe_reports += 1

    print(f"Amount of safe reports {amount_of_safe_reports}")
    return amount_of_safe_reports


def read_file(path: str) -> List[int]:
    with open(path) as input_file:
        numbers = []
        for line in input_file:
            numbers.append([int(i) for i in line.split()])
        return numbers


if __name__ == "__main__":
    main(FILE_PATH)

import os
from typing import List


FILE_PATH = "input"


# The second solution is the same as the first, but we loop over all the possible lists when you remove 1 element and do the same checks
def main(path) -> int:
    full_path = os.path.join(os.path.dirname(__file__), path)
    number_lists = read_file(full_path)

    amount_of_safe_reports = 0
    for number_list in number_lists:
        has_safe_variant = False
        for i in range(len(number_list)):
            copy_list = number_list.copy()
            copy_list.pop(i)
            is_safe = is_safe_report(copy_list)
            if is_safe:
                has_safe_variant = True

        if has_safe_variant:
            amount_of_safe_reports += 1

    print(f"Amount of safe reports {amount_of_safe_reports}")
    return amount_of_safe_reports


def is_safe_report(number_list: List[int]):
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

    return is_safe


def read_file(path: str) -> List[List[int]]:
    with open(path) as input_file:
        numbers = []
        for line in input_file:
            numbers.append([int(i) for i in line.split()])
        return numbers


if __name__ == "__main__":
    main(FILE_PATH)

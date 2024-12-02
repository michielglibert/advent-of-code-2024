import os
from typing import List, Tuple

FILE_PATH = "input"


def main():
    full_path = os.path.join(os.path.dirname(__file__), FILE_PATH)
    numbers = read_file(full_path)
    list_1, list_2 = create_lists(numbers)

    # Being lazy and using python sort
    list_1.sort()
    list_2.sort()

    total_distance = 0
    for i in range(len(list_1)):
        total_distance += abs(list_1[i] - list_2[i])

    print(f"Total distance is {total_distance}")


def create_lists(numbers: List[str]) -> Tuple[List[str], List[str]]:
    """Lists are created by rotating between them while looping over the numbers"""
    list_1 = []
    list_2 = []
    for i in range(0, len(numbers), 2):
        list_1.append(numbers[i])
        list_2.append(numbers[i + 1])
    return (list_1, list_2)


def read_file(path: str) -> List[str]:
    with open(path) as input_file:
        numbers = []
        for line in input_file:
            numbers.extend([int(i) for i in line.split()])
        return numbers


if __name__ == "__main__":
    main()

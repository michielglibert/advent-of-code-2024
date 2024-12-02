import os
from typing import List, Tuple

FILE_PATH = "input"


def main():
    full_path = os.path.join(os.path.dirname(__file__), FILE_PATH)
    numbers = read_file(full_path)
    list_1, list_2 = create_lists(numbers)

    similarity_score = 0
    counter = {key: 0 for key in list_2}
    for num in list_2:
        counter[num] += 1

    for num in list_1:
        occurences = counter.get(num)
        if occurences is not None:
            similarity_score += num * occurences

    print(f"The similarity score is {similarity_score}")


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

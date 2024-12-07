from functools import reduce
from typing import Dict, List, Tuple

FILE_PATH = "input"

OPERATORS = ("+", "*")


def do_operation(operator, a: int, b: int) -> int:
    match operator:
        case "+":
            return a + b
        case "*":
            return a * b
        case _:
            raise Exception


def main(path):
    numbers_lists = read_file(path)

    correct_calibrations = []
    for result, numbers in numbers_lists:
        n = len(numbers) - 1
        combinations = 2**n

        # Loop over combinations
        for i in range(combinations):
            binary = format(i, f"0{n}b")
            operators = [OPERATORS[1] if bit == "1" else OPERATORS[0] for bit in binary]

            value = numbers[0]
            for idx, operator in enumerate(operators, start=1):
                value = do_operation(operator, value, numbers[idx])

            if value == result:
                correct_calibrations.append(result)
                break

    print(reduce(lambda a, b: a + b, correct_calibrations, 0))


def read_file(path: str) -> List[Tuple[int, List[int]]]:
    with open(path) as input_file:
        result = []
        for line in input_file:
            split = line.split(":")
            key = int(split[0])
            values = [int(number) for number in split[1].strip().split(" ")]
            result.append((key, values))
        return result


if __name__ == "__main__":
    main(FILE_PATH)

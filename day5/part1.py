from collections import defaultdict
import os
import re
from typing import List


FILE_PATH = "input"


def main(path):
    orders, updates = read_file(path)

    order_dict = defaultdict(list)
    for order in orders:
        order_dict[order[0]].append(order[1])

    valid_updates = []

    for update in updates:
        is_valid = True
        for i in range(1, len(update)):
            to_be_checked_array = update[:i]
            for number in to_be_checked_array:
                if number in order_dict[update[i]]:
                    is_valid = False

        if is_valid:
            valid_updates.append(update)

    sum = 0
    for valid_update in valid_updates:
        middle_index = len(valid_update) // 2
        sum += valid_update[middle_index]

    print(sum)


def read_file(path: str):
    orders = []
    updates = []
    with open(path) as input_file:
        for line in input_file:
            if "|" in line:
                tuples_values = tuple(map(int, line.split("|")))
                orders.append(tuples_values)
            elif "," in line:
                number_values = list(map(int, line.split(",")))
                updates.append(number_values)
    return (orders, updates)


if __name__ == "__main__":
    main(FILE_PATH)

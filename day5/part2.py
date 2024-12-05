from collections import defaultdict
import functools


FILE_PATH = "input"


def main(path):
    orders, updates = read_file(path)

    order_dict = defaultdict(list)
    for order in orders:
        order_dict[order[0]].append(order[1])

    invalid_updates = []

    for update in updates:
        is_valid = True
        for i in range(1, len(update)):
            to_be_checked_array = update[:i]
            for number in to_be_checked_array:
                if number in order_dict[update[i]]:
                    is_valid = False

        if not is_valid:
            invalid_updates.append(update)

    # Define custom_sort inside main to access order_dict
    def custom_sort(a, b):
        if b in order_dict[a]:
            return -1  # u1 should come before u2
        if a in order_dict[b]:
            return 1  # u1 should come after u2
        return 0

    sorted_invalid_updates = []
    for update in invalid_updates:
        sorted_invalid_updates.append(
            sorted(update, key=functools.cmp_to_key(custom_sort))
        )

    sum = 0
    for invalid_update in sorted_invalid_updates:
        middle_index = len(invalid_update) // 2
        sum += invalid_update[middle_index]

    print(sum)


def custom_sort(order_dict, a, b):
    if b in order_dict[a]:
        return 1
    else:
        return 0


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

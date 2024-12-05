import os
import re
from typing import List


FILE_PATH = "input"


def main(path):
    grid = read_file(path)

    total = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            total += check_grid(grid, y, x)

    print(total)


def check_grid(grid, y, x) -> int:
    if grid[y][x] != "A":
        return 0
    try:
        # Ensure all required indices are within bounds
        rows, cols = len(grid), len(grid[0])
        if not (0 <= y - 1 < rows and 0 <= x - 1 < cols):
            return 0
        if not (0 <= y + 1 < rows and 0 <= x + 1 < cols):
            return 0
        if not (0 <= y + 1 < rows and 0 <= x - 1 < cols):
            return 0
        if not (0 <= y - 1 < rows and 0 <= x + 1 < cols):
            return 0

        word = ""
        word += grid[y - 1][x - 1]
        word += "A"
        word += grid[y + 1][x + 1]
        if word != "SAM" and word != "MAS":
            return 0

        word = ""
        word += grid[y + 1][x - 1]
        word += "A"
        word += grid[y - 1][x + 1]
        if word != "SAM" and word != "MAS":
            return 0

        return 1
    except IndexError:
        return 0


def read_file(path: str) -> List[List[str]]:
    with open(path) as input_file:
        grid = [list(line.strip()) for line in input_file]
    return grid


if __name__ == "__main__":
    main(FILE_PATH)

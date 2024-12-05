import os
import re
from typing import List


FILE_PATH = "input"


def main(path):
    grid = read_file(path)

    total = 0
    directions = [
        (-1, -1),  # LeftUp
        (0, -1),  # Left
        (1, -1),  # LeftDown
        (-1, 1),  # RightUp
        (0, 1),  # Right
        (1, 1),  # RightDown
        (-1, 0),  # Up
        (1, 0),  # Down
    ]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for vertical_step, horizontal_step in directions:
                total += check_grid(grid, y, x, vertical_step, horizontal_step)

    print(total)


def check_grid(grid, y, x, vertical_step, horizontal_step) -> int:
    """Vertical step should be -1 for up, 0 for none and 1 for down"""
    """Horizontal step should be -1 for left, 0 for none and 1 for right"""
    try:
        for i, letter in enumerate("XMAS"):
            new_y = y + i * vertical_step
            new_x = x + i * horizontal_step
            if new_y < 0 or new_x < 0 or grid[new_y][new_x] != letter:
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

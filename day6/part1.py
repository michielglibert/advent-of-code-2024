from collections import defaultdict
from typing import List, Tuple


FILE_PATH = "input"


class Map:
    # (VERTICAL, HORIZONTAL)
    # Vertical step should be -1 for up, 0 for none and 1 for down
    # Horizontal step should be -1 for left, 0 for none and 1 for right
    orientations = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )
    current_orientation_index = 0

    def __init__(self, grid) -> None:
        self.grid = grid
        self.current_position = self.find_starting_position()
        self.visited_positions = set()
        self.visited_positions.add(self.current_position)

    def find_starting_position(self) -> Tuple[int, int]:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == "^":
                    return (y, x)

    def do_step(self) -> bool:
        """Will return True if not yet out of bounds"""
        try:
            new_y = (
                self.current_position[0]
                + self.orientations[self.current_orientation_index][0]
            )
            new_x = (
                self.current_position[1]
                + self.orientations[self.current_orientation_index][1]
            )

            if self.can_step(new_y, new_x):
                # We need to access to grid so that we can trigger an IndexError
                self.grid[new_y][new_x]
                self.current_position = (new_y, new_x)
                self.visited_positions.add(self.current_position)
            else:
                self.rotate_right_90_degrees()
        except IndexError:
            return False

        return True

    def rotate_right_90_degrees(self):
        self.current_orientation_index = (self.current_orientation_index + 1) % 4

    def can_step(self, y, x) -> bool:
        try:
            if self.grid[y][x] == "#":
                return False
        except IndexError:
            return True
        return True

    def get_distinct_positons(self):
        return len(self.visited_positions)


def main(path):
    grid = read_file(path)

    map = Map(grid)

    while map.do_step():
        pass

    print(map.get_distinct_positons())


def read_file(path: str) -> List[List[str]]:
    with open(path) as input_file:
        return [list(line.strip()) for line in input_file]


if __name__ == "__main__":
    main(FILE_PATH)

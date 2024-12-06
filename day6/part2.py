from collections import defaultdict
import copy
from typing import List, Tuple


FILE_PATH = "input"


class Map:
    orientations = (
        (-1, 0),  # up
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
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
        dy, dx = self.orientations[self.current_orientation_index]
        new_y = self.current_position[0] + dy
        new_x = self.current_position[1] + dx

        if not (0 <= new_y < len(self.grid) and 0 <= new_x < len(self.grid[0])):
            return False  # guard left the area

        if self.grid[new_y][new_x] in ("#", "O"):
            self.rotate_right_90_degrees()
            return True

        self.current_position = (new_y, new_x)
        self.visited_positions.add(self.current_position)
        return True

    def rotate_right_90_degrees(self):
        self.current_orientation_index = (self.current_orientation_index + 1) % 4

    def get_distinct_positions(self):
        return len(self.visited_positions)

    def add_collision(self, y, x):
        self.grid[y][x] = "O"

    def check_for_loop(self) -> bool:
        visited_states = set()
        while True:
            state = (
                self.current_position[0],
                self.current_position[1],
                self.current_orientation_index,
            )
            if state in visited_states:
                return True
            visited_states.add(state)

            can_continue = self.do_step()
            if not can_continue:
                return False


def main(path):
    grid = read_file(path)

    part1_map = Map(copy.deepcopy(grid))

    guard_starting_position = part1_map.current_position

    while part1_map.do_step():
        pass

    possible_collision_locations = part1_map.visited_positions.copy()
    possible_collision_locations.remove(guard_starting_position)

    looped = 0
    for collision in possible_collision_locations:
        test_map = Map(copy.deepcopy(grid))
        test_map.add_collision(collision[0], collision[1])
        if test_map.check_for_loop():
            looped += 1

    print(looped)


def read_file(path: str) -> List[List[str]]:
    with open(path) as input_file:
        return [list(line.rstrip("\n")) for line in input_file]


if __name__ == "__main__":
    main(FILE_PATH)

from collections import defaultdict
import copy
from typing import List, Tuple


FILE_PATH = "input"

# Put collisions on path walked in part 1
# Find loop by checking if collision is found again with same direction


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
    has_collision = False
    last_collision = None

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

    def do_step(self) -> Tuple[bool, bool]:
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
                if self.grid[new_y][new_x] == "O" and self.has_collision:
                    collision_location = (
                        (new_y, new_x),
                        self.current_orientation_index,
                    )
                    if self.last_collision:
                        if self.last_collision == collision_location:
                            return False, True
                    else:
                        self.last_collision = collision_location

                self.rotate_right_90_degrees()
        except IndexError:
            return False, False

        return True, False

    def rotate_right_90_degrees(self):
        self.current_orientation_index = (self.current_orientation_index + 1) % 4

    def can_step(self, y, x) -> bool:
        try:
            if self.grid[y][x] == "#" or self.grid[y][x] == "O":
                return False
        except IndexError:
            return True
        return True

    def get_distinct_positons(self):
        return len(self.visited_positions)

    def add_collision(self, y, x):
        self.grid[y][x] = "O"
        self.has_collision = True

    def check_for_loop(self) -> bool:
        max_n = sum(len(row) for row in self.grid)
        step_result = self.do_step()
        i = 0
        while step_result[0] and i < max_n + 1:
            i += 1
            step_result = self.do_step()

        if step_result[1] == True or i >= max_n:
            return True
        return False


def main(path):
    grid = read_file(path)

    part1_map = Map(grid)
    collision_map = Map(grid)

    guard_starting_position = part1_map.find_starting_position()

    while part1_map.do_step()[0]:
        pass

    # Put collisions on walked path
    possible_collision_locations = part1_map.visited_positions.copy()
    possible_collision_locations.remove(guard_starting_position)

    looped = 0
    for collision in possible_collision_locations:
        map = copy.deepcopy(collision_map)
        map.add_collision(collision[0], collision[1])
        print(looped)
        if map.check_for_loop():
            looped += 1

    print(looped)


def read_file(path: str) -> List[List[str]]:
    with open(path) as input_file:
        return [list(line.strip()) for line in input_file]


if __name__ == "__main__":
    main(FILE_PATH)

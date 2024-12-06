from typing import List
from pyutil.cardinal_direction import Direction
from pyutil.fileio import file_lines
from pyutil.grids import col_count, is_valid_coord, row_count, walk


class Solution:

    def find_start_pos(self, grid, search_marker: str):
        n = row_count(grid)
        for r in range(n):
            for c in range(n):
                if grid[r][c] == search_marker:
                    return r, c
        raise SystemError("start pos not found")

    def computeDay(self, grid: List[str], part: int):
        assert row_count(grid) == col_count(grid), "error: grid not square"
        for line in grid:
            print(line)
        is_obstacle = lambda grid, r, c: grid[r][c] == "#"
        is_off_edge = lambda grid, r, c: not is_valid_coord(grid, r, c)

        # start facing north
        r, c = self.find_start_pos(grid, "^")
        direction = Direction.North

        # fmt:off
        can_walk = lambda grid, r, c: (not is_off_edge(grid, r, c)) and \
                                      (not is_obstacle(grid, r, c))
        get_coord = lambda _, r, c: (r,c)
        # fmt:on

        # walk
        points = []
        while True:
            points_, end_pos = walk(grid, r, c, direction, can_walk, get_coord)
            points += points_
            end_r, end_c = end_pos
            if not is_valid_coord(grid, end_r, end_c):
                break
            r, c = direction.walk_backward(end_r, end_c)  # last valid point
            direction = direction.turn_right()  # turn

        count = len(set(points))
        return count


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2024/input/06_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2024/input/06_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()

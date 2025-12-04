from typing import List
from pyutil.fileio import file_lines
from pyutil.grids import search


class Solution:
    def computeDay(self, lines: List[str], part: int):
        grid = [list(line) for line in lines]

        def fewer_than_4_adjacent_rolls(grid, origin, neighbors):
            if grid[origin[0]][origin[1]] == ".":
                return False
            roll_count = sum(1 for r, c in neighbors if grid[r][c] == "@")
            return roll_count < 4

        if part == 1:
            return len(search(grid, query=fewer_than_4_adjacent_rolls))
        else:
            total_removed = 0
            removable = True
            while removable:
                removable = search(grid, query=fewer_than_4_adjacent_rolls)
                if removable:
                    for r, c in removable:
                        grid[r][c] = "."
                    total_removed += len(removable)
            return total_removed


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/04_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/04_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()

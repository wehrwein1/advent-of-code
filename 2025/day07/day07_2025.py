from functools import cache
from typing import List
from pyutil.cardinal_direction import Direction
from pyutil.fileio import file_lines
from pyutil.grids import dim, is_valid_coord


class Solution:
    def computeDay(self, lines: List[str], part: int):
        if part == 2:
            return self.part2(lines)

        # part 1
        can_walk = is_valid_coord

        def tachyon_beam(r: int, c: int, dir: Direction, count: int, indent=0):
            while can_walk(grid, r, c):
                value = grid[r][c]
                if value == "|":  # is visited
                    return count
                grid[r][c] = "|"  # mark visited
                if value == "^":
                    # print(f"{indent * ' '} split {r} {c} _ {count}")
                    count = tachyon_beam(r, c - 1, dir, count, indent + 1)
                    count = tachyon_beam(r, c + 1, dir, count, indent + 1)
                    count += 1  # postorder = no double counting
                    print(f"{indent * ' '} join  {r} {c} _ {count}")
                else:
                    r, c = dir.walk_forward(r, c)
            return count

        grid = [list(line) for line in lines]
        r = 0
        c = grid[0].index("S")
        print(f"dim   {dim(grid)}")
        print(f"start {r} {c}")
        split_count = tachyon_beam(r, c, Direction.South, 0)
        print()
        for row in grid:  # show paths
            print(row)
        return split_count

    def part2(self, lines: List[str]):
        # so simple! wow. From https://www.reddit.com/r/adventofcode/comments/1pg9w66/comment/nsr76g5
        grid = [list(line) for line in lines]

        @cache
        def dfs(i, j):
            while grid[i][j] == ".":
                i += 1
                if i == len(grid):
                    return 1
            return dfs(i, j - 1) + dfs(i, j + 1)

        return dfs(1, grid[0].index("S"))


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/07_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/07_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()

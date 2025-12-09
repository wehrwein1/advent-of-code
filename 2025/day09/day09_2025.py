import itertools
from typing import List
from pyutil.fileio import file_lines


class Solution:

    def computeDay(self, lines: List[str], part: int):
        def manhattan_distance(a, b):
            return abs(b[0] - a[0]) + abs(b[1] - a[1])

        if part == 2:
            return  # not implemented

        points = [list(map(int, line.split(","))) for line in lines]

        # check pairwise
        max_distance = -1
        max_corners = []
        for combo in itertools.combinations(points, 2):
            d = manhattan_distance(combo[0], combo[1])
            if d > max_distance:
                max_distance = d
                max_corners = combo

        # compute area
        print(f"{max_distance=}, {max_corners=}")
        x_values = [point[0] for point in max_corners]
        y_values = [point[1] for point in max_corners]
        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        INCLUSIVE: int = 1
        width = x_max - x_min + INCLUSIVE
        height = y_max - y_min + INCLUSIVE
        return width * height


# bootstrap
def main():
    print(f"part 1: {Solution().computeDay(file_lines('2025/input/09_INPUT.txt'), 1)}")
    print(f"part 2: {Solution().computeDay(file_lines('2025/input/09_INPUT.txt'), 2)}")


if __name__ == "__main__":
    main()

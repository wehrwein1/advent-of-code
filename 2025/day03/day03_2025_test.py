from day03_2025 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2025/input/03_TEST.txt"), 1) == 357


def test_part2():
    assert (
        Solution().computeDay(file_lines("2025/input/03_TEST.txt"), 2) == 3121910778619
    )

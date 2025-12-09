from day09_2025 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2025/input/09_TEST.txt"), 1) == 50


def ignore_test_part2():
    assert Solution().computeDay(file_lines("2025/input/09_TEST.txt"), 2) == -1

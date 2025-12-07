from day07_2025 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2025/input/07_TEST.txt"), 1) == 21


def test_part2():
    assert Solution().computeDay(file_lines("2025/input/07_TEST.txt"), 2) == 40

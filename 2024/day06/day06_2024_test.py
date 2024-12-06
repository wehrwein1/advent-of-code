from day06_2024 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2024/input/06_TEST.txt"), 1) == 41


def skip_test_part2():
    assert Solution().computeDay(file_lines("2024/input/06_TEST.txt"), 2) == -1

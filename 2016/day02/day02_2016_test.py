from day02_2016 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2016/input/02_TEST.txt"), 1) == 1985


def ignore_test_part2():
    assert Solution().computeDay(file_lines("2016/input/02_TEST.txt"), 2) == -1

from day05_2025 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2025/input/05_TEST.txt"), 1) == 3


def test_part2():
    assert Solution().overlap((3, 5), (10, 14)) == 0
    assert Solution().overlap((10, 14), (12, 18)) == 3
    assert Solution().overlap((16, 20), (12, 18)) == 3
    assert Solution().range_len((3, 5)) == 3
    assert Solution().range_len((10, 14)) == 5

    assert Solution().computeDay(file_lines("2025/input/05_TEST.txt"), 2) == 14


def test_part2_alt1():
    assert Solution().computeDay(file_lines("2025/input/05_TEST1.txt"), 2) == 14


def test_part2_alt2():
    assert Solution().computeDay(file_lines("2025/input/05_TEST2.txt"), 2) == 18

from day05_2025 import Solution
from pyutil.fileio import file_lines


def test_part1():
    assert Solution().computeDay(file_lines("2025/input/05_TEST.txt"), 1) == 3


def test_part2():
    assert Solution().range_len((3, 5)) == 3
    assert Solution().range_len((10, 14)) == 5

    assert Solution().computeDay(file_lines("2025/input/05_TEST.txt"), 2) == 14


def test_part2_alt1():
    assert Solution().computeDay(["3-5", "10-14", "19-20", "12-18", ""], 2) == 14


def test_part2_alt2():
    # fmt:off
    assert Solution().computeDay(["3-5", "10-14", "19-20", "12-18", "17-19", ""], 2) == 14
    # fmt:on


def test_part2_alt3():
    assert Solution().computeDay(["3-11", "10-14", "19-20", "12-18", ""], 2) == 18


def test_part2_alt4():
    assert Solution().computeDay(["3-5", "8-12", "9-11", ""], 2) == 3 + 5

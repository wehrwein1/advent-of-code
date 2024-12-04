from day03 import Solution, readlines


def test_part1():
    assert Solution().computeDay(readlines("2024/input/03_TEST1.txt"), 1) == 161


def test_part2():
    assert Solution().computeDay(readlines("2024/input/03_TEST2.txt"), 2) == 48

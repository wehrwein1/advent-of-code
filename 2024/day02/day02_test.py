from day02 import Solution, readlines


def test_part1():
    assert Solution().computeDay(readlines("2024/input/02_TEST.txt"), 1) == 2


def test_part2():
    assert Solution().computeDay(readlines("2024/input/02_TEST.txt"), 2) == 4

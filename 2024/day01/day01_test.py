from day01 import Solution


def test_part1():
    assert Solution().computeDay(open('2024/input/01_TEST.txt').readlines(), 1) == 11


def test_part2():
    assert Solution().computeDay(open('2024/input/01_TEST.txt').readlines(), 2) == 31

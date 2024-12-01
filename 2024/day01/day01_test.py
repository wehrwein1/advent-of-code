from day01 import Solution

def test_part1():
  assert Solution().computeDay(list(map(str.rstrip, open('2024/input/01_TEST.txt'))), 1) == 11

def test_part2():
  assert Solution().computeDay(list(map(str.rstrip, open('2024/input/01_TEST.txt'))), 2) == 31
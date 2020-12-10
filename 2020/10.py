# https://adventofcode.com/2020/day/10
from typing import Callable, List
from collections import defaultdict
from functools import reduce

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def load_joltages(filename, wall_joltage = 0): 
  joltages = sorted(map(int, load_file(filename)))
  my_device_handles = max(joltages) + 3
  return [wall_joltage] + joltages + [my_device_handles]
  
def compute_joltage_diffs(joltages : List[int]) -> List[int]:
  diffs = []
  for i, joltage in enumerate(joltages):
    if i == 0: continue
    diffs.append(joltage - joltages[i-1])
  return diffs
assert_equals(compute_joltage_diffs(load_joltages('input/10_TEST_small.txt')), [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3])
assert_equals(compute_joltage_diffs(load_joltages('input/10_TEST.txt')), [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3])

def compute_joltage_diff_counts(joltages : List[int]) -> int:
  diff_counts = defaultdict(int)
  for diff in compute_joltage_diffs(joltages):
    max_counted_diff = 3 if diff >= 3 else 1 if diff >= 1 else 0
    diff_counts[max_counted_diff] += 1
  return diff_counts
assert_equals(compute_joltage_diff_counts(load_joltages('input/10_TEST_small.txt')), { 1 : 7, 3 : 5})
assert_equals(compute_joltage_diff_counts(load_joltages('input/10_TEST.txt')), { 1 : 22, 3 : 10})
# part 1
diff_counts = compute_joltage_diff_counts(load_joltages('input/10_INPUT.txt'))
product = reduce((lambda x, y: x * y), diff_counts.values())
print("part 1: product of joltage counts:", product)

# part 2
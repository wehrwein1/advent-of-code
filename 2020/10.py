# https://adventofcode.com/2020/day/10
from typing import Callable, List
from collections import defaultdict
from functools import reduce

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def load_joltages(filename):          return sorted([int(line) for line in load_file(filename)])

def compute_joltage_diffs(joltages : List[int], wall_joltage = 0) -> int:
  my_device_handles = max(joltages) + 3
  joltages.insert(0, wall_joltage)
  joltages.append(my_device_handles)
  diff_counts = defaultdict(int)
  for i, joltage in enumerate(joltages):
    if (i == 0): continue
    diff = joltage - joltages[i-1]
    # print('joltage[{}]: {}, diff={}'.format(i, joltage, diff))
    max_counted_diff = 3 if diff >= 3 else 1 if diff >= 1 else 0
    diff_counts[max_counted_diff] += 1
  # for diff, count in diff_counts.items():
  #   print('diff={}, count={}'.format(diff, count)) 
  return diff_counts
assert_equals(compute_joltage_diffs(load_joltages('input/10_TEST.txt')), { 1 : 22, 3 : 10})
  
# part 1
diff_counts = compute_joltage_diffs(load_joltages('input/10_INPUT.txt'))
product = reduce((lambda x, y: x * y), diff_counts.values())
print("part 1: product of joltage counts:", product)

# part 2
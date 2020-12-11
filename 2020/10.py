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

def product(numbers : List[int]) -> int: 
  return reduce((lambda x, y: x * y), numbers)
assert_equals(product([2,3]), 6)
assert_equals(product([2,3,4,5,6]), 720)
  
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
  
def compute_adjacency_lists(joltages : List[int]) -> List[int]:
  diffs = compute_joltage_diffs(joltages)
  source_to_targets = dict()
  # print("joltages:", joltages)
  # print("diffs:   ", diffs)
  for i, diff in enumerate(diffs):
    joltage = joltages[i]
    diff = diffs[i]
    branches = [val for val in joltages[i:] if (val > joltage and val <= joltage + 3)]
    # print('joltages[{}]: diff={}, value={} -> {}'.format(i, diff, joltage, branches))
    source_to_targets[joltage] = branches
  return source_to_targets
assert_equals(compute_adjacency_lists(load_joltages('input/10_TEST_small.txt')), {0:[1], 1:[4], 4:[5,6,7], 5:[6,7], 6:[7], 7:[10], 10:[11,12], 11:[12], 12:[15], 15:[16], 16:[19], 19:[22]})

def count_paths(joltages : List[int]) -> int:
  source_to_targets = compute_adjacency_lists(joltages)
  # print("source_to_targets=", source_to_targets)
  branch_counts = dict()
  for source, targets in reversed(source_to_targets.items()):
    value = 0 
    for target in targets:
      if target in branch_counts:
        value += branch_counts[target]
    # print('source={}, targets={}, value={}'.format(source, targets, value))
    branch_counts[source] = value if value > 0 else 1
  return branch_counts[0]
assert_equals(count_paths(load_joltages('input/10_TEST_small.txt')), 8)
assert_equals(count_paths(load_joltages('input/10_TEST.txt')), 19208)

diff_counts = compute_joltage_diff_counts(load_joltages('input/10_INPUT.txt'))
print("part 1: product of joltage counts:", product(diff_counts.values()))
print('part 2: paths count:', count_paths(load_joltages('input/10_INPUT.txt')))
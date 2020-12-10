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
  
def compute_branch_counts(joltages : List[int]) -> List[int]:
  diffs = compute_joltage_diffs(joltages)
  branch_counts = []
  print("joltages:", joltages)
  print("diffs:   ", diffs)
  for i, diff in enumerate(diffs):
    joltage = joltages[i]
    diff = diffs[i]
    branches = [val for val in joltages[i:] if (val > joltage and val <= joltage + 3)]
    print('joltages[{}]: diff={}, value={} -> {}'.format(i, diff, joltage, branches))
    branch_counts.append(len(branches))
  return branch_counts
assert_equals(compute_branch_counts(load_joltages('input/10_TEST_small.txt')), [1,1,3,2,1,1,2,1,1,1,1,1])

def count_paths(joltages : List[int]) -> int:
  branch_counts = compute_branch_counts(joltages)
  print("branch counts=", branch_counts)
  total, i, j = 0, 0, 0
  have_i = False
  while i < len(branch_counts):
    try:
      print('start loop i={}'.format(i))
      while branch_counts[i] == 1: i+= 1
      print(' i={}, value={}'.format(i, branch_counts[i]))
      j = i + 1
      have_i = True
      while branch_counts[j] == 1: j+= 1
      print(' j={}, value={}'.format(j, branch_counts[j]))
      total += product(branch_counts[i:j+1])
      print(' non-zero values in indices {}-{}: {}, new sum={}'.format(i,j, branch_counts[i:j+1], total))
      i = j + 1
    except IndexError:
      print('errored out on i={}, j={}, have_i={}'.format(i,j, have_i))
      if have_i: 
        print('finalize i value, total += {}'.format(branch_counts[i]))
        total += branch_counts[i]
      return total
  return total
assert_equals(count_paths(load_joltages('input/10_TEST_small.txt')), 8)
assert_equals(count_paths(load_joltages('input/10_TEST.txt')), 19208)

diff_counts = compute_joltage_diff_counts(load_joltages('input/10_INPUT.txt'))
print("part 1: product of joltage counts:", product(diff_counts.values()))
print('part 2: paths:', count_paths(load_joltages('input/10_INPUT.txt')))
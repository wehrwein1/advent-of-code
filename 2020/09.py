# https://adventofcode.com/2020/day/9
from typing import List

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

def load_file(filename): 
  return [int(line) for line in map(str.rstrip, open(filename))]

def compute_all_sums(numbers):
  sums = []
  for i in range(len(numbers)):
    for j in range(len(numbers)):
      if i != j: 
        sums.append((numbers[i] + numbers[j]))
  return sums

# functions
def find_non_sum_number(preamble_length : int, lines : List[str]) -> int:
  for i in range(preamble_length, len(lines)):
    preamble = lines[i-preamble_length:i+1]
    num = lines[i]
    # print('i={}, num={}, preamble={}'.format(i, num, preamble))
    if num not in compute_all_sums(preamble):
      # print('part 1:', num)
      return num
assert_equals(find_non_sum_number(preamble_length=5, lines=load_file('input/09_TEST.txt')), 127)

def find_encryption_weakness(invalid_num : int, lines : List[str]) -> int:
  i = 0
  while i < len(lines):
    search_range = list()
    j = i
    while sum(search_range) < invalid_num:
      search_range.append(lines[j])
      j += 1
    # print('i={}, j={}, search_range={}, sum={}'.format(i, j, search_range, sum(search_range)))
    if sum(search_range) == invalid_num:
      # print('part 2:', search_range)
      return min(search_range) + max(search_range)
    i += 1
assert_equals(find_encryption_weakness(invalid_num=127, lines=load_file('input/09_TEST.txt')), 62)

lines = load_file('input/09_INPUT.txt'); #print('\ninput (len={}): {}'.format(len(lines), lines))
invalid_number = find_non_sum_number(preamble_length=25, lines=lines)
print('part 1:', invalid_number)
print('part 2:', find_encryption_weakness(invalid_num=invalid_number, lines=lines))
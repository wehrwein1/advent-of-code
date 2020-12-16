# https://adventofcode.com/2020/day/16
from typing import List, Dict
from collections import defaultdict

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]

# decode your train ticket
# ticket field validation, ranges are inclusive
# have ticket field values (#) but not field names (???)
# find sum of numbers for which no rule is valid "ticket scanning error rate"

def find_error_tickets(lines : List[str]) -> int:
  field_specs =    [line for i, line in enumerate(lines) if i < lines.index('your ticket:') - 1]
  nearby_tickets = [line for i, line in enumerate(lines) if i > lines.index('nearby tickets:')]
  print("fields_specs:", field_specs)
  field_ranges = defaultdict(list)
  for field_spec in field_specs:
    tokens = field_spec.split(': ', 1)
    field_name = tokens[0]
    print("field_name: '{}'".format(field_name))
    for range_spec in tokens[1].split(' or '):
      print("range_spec: '{}'".format(range_spec))
      low, high = map(int, range_spec.split('-'))
      field_ranges[field_name].append(range(low, high + 1))
  print("field ranges:", field_ranges)
  print('nearby:', nearby_tickets)
  nums = []
  for tickets in nearby_tickets:
    nums.extend(map(int, tickets.split(',')))
  print('nums:', nums)

  def is_in_any_range(num : int, all_ranges):
    for ranges in field_ranges.values():
      for field_range in ranges:
        if num in field_range: 
          print('num {} in range {}'.format(num, field_range))
          return True
    print('num {} not in any range'.format(num))
    return False

  print(field_ranges.values())
  # exit()
  error_tickets = [num for num in nums if not is_in_any_range(num, field_ranges.values())]
  return error_tickets
assert_equals(find_error_tickets(load_file('input/16_TEST.txt')), [4, 55, 12])
assert_equals(sum(find_error_tickets(load_file('input/16_TEST.txt'))), 71)
assert_equals(sum(find_error_tickets(load_file('input/16_INPUT.txt'))), 71)
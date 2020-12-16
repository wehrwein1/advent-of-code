# Disclaimer: given that AoC is a speed-based challenge, this code is optimized for development and debugging speed 
# not maintainability. In general, maintainability/understandability is the primary cost driver of software overall 
# -- I've written about this previously: https://ieeexplore.ieee.org/abstract/document/6650541. This is not 
# necessarility reflective of what I consider "good" production-quality code. Would be an exercise to simplify, 
# reduce duplication, optimize big O runtime performance, and make it more self-documenting.

# https://adventofcode.com/2020/day/16
from typing import List, Dict, Tuple
from collections import defaultdict
from functools import reduce

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def product(numbers : List[int]):     return reduce(lambda x, y: x * y, numbers)

# part 1:
# decode your train ticket
# ticket field validation, ranges are inclusive
# have ticket field values (#) but not field names (???)
# find sum of numbers for which no rule is valid "ticket scanning error rate"

# part 2:
# discard invalid tickets
# apply validation ranges across all tickets, find correct field order
# return your ticket, then product all 'departure' field values

def find_error_ticket_fields(lines : List[str]) -> Tuple[List[int], Dict]:
  field_specs =    [line for i, line in enumerate(lines) if i < lines.index('your ticket:') - 1]
  nearby_tickets = [line for i, line in enumerate(lines) if i > lines.index('nearby tickets:')]
  # print("fields_specs:", field_specs)
  field_ranges = defaultdict(list)
  for field_spec in field_specs:
    tokens = field_spec.split(': ', 1)
    field_name = tokens[0]
    # print("field_name: '{}'".format(field_name))
    for range_spec in tokens[1].split(' or '):
      # print("range_spec: '{}'".format(range_spec))
      low, high = map(int, range_spec.split('-'))
      field_ranges[field_name].append(range(low, high + 1))
  # print("field ranges:", field_ranges)
  # print('nearby:', nearby_tickets)
  nums = []
  for tickets in nearby_tickets:
    nums.extend(map(int, tickets.split(',')))
  # print('nums:', nums)

  def is_in_any_range(num : int, all_ranges : List[List]):
    for ranges in all_ranges:
      # print('ranges:', ranges)
      for field_range in ranges:
        # print('field_range:', field_range)
        if num in field_range: 
          # print('num {} in range {}'.format(num, field_range))
          return True
    # print('num {} not in any range'.format(num))
    return False

  error_tickets = [num for num in nums if not is_in_any_range(num, field_ranges.values())]
  return error_tickets, field_ranges
assert_equals(find_error_ticket_fields(load_file('input/16_TEST.txt'))[0], [4, 55, 12])
assert_equals(sum(find_error_ticket_fields(load_file('input/16_TEST.txt'))[0]), 71)

def find_my_ticket(lines : List[str]):
  # discard tickets containing error fields
  error_fields, field_ranges = find_error_ticket_fields(lines)
  nearby_tickets = [list(map(int, line.split(','))) for i, line in enumerate(lines) if i > lines.index('nearby tickets:')]
  # print('nearby (len={}): many'.format(len(nearby_tickets), nearby_tickets))
  nearby_tickets = [nearby_ticket for nearby_ticket in nearby_tickets if (not any([invalid_field in nearby_ticket for invalid_field in error_fields])) ]
  # print('nearby (len={}): {}'.format(len(nearby_tickets), nearby_tickets))

  def is_in_any_range(num : int, all_ranges : List[List]):
    for field_range in all_ranges:
      # print('field_range:', field_range)
      if num in field_range: 
        # print('num {} in range {}'.format(num, field_range))
        return True
    # print('num {} not in any range'.format(num))
    return False

  # print('field ranges:')
  # for ticket_index, possible_fields in field_ranges.items():
  #   print('i={}: {}'.format(ticket_index, possible_fields))

  # find fields that could be valid for each field index
  number_of_fields = len(nearby_tickets[0])
  index_fields : Dict[int, List[int]] = defaultdict(set)
  for ticket_field_index in range(0, number_of_fields):
    all_ticket_field_values = [ticket_fields[ticket_field_index] for ticket_fields in nearby_tickets]
    # print("ticket index i={}, values: {}".format(ticket_field_index, all_ticket_field_values))
    for field_name, allowed_ranges in field_ranges.items():
      # print("field '{}' must in one of {}".format(field_name, allowed_ranges))
      if all([is_in_any_range(value, allowed_ranges) for value in all_ticket_field_values]):
        # print("ticket index {} could be '{}'".format(ticket_field_index, field_name))
        index_fields[ticket_field_index].add(field_name)
  
  # print('index_fields:', index_fields)
  # for ticket_index, possible_fields  in index_fields.items():
  #   print('i={}: {}'.format(ticket_index, possible_fields))
  
  # iteratively choose fields, setting fields for which only one choice, eliminating taken choices each step until all done
  field_indices : Dict[str, int]= dict()
  while len(field_indices) < number_of_fields:
    for ticket_index, possible_fields  in index_fields.items():
      if len(possible_fields) == 1:
        field_name = list(possible_fields)[0]
        # print('index {} is {}'.format(ticket_index, field_name))
        field_indices[field_name] = ticket_index
        del index_fields[ticket_index]
        # print('updated index_fields: {}'.format(index_fields))
        # print('updated field_indices: {}'.format(field_indices))
        for ticket_index, possible_fields  in index_fields.items():
          possible_fields.remove(field_name)
        break
  # print('field_indices:', field_indices)
  
  # decode my ticket using indices
  my_ticket_values = list(map(int, lines[lines.index('your ticket:')+1].split(',')))
  # print('my_ticket:', my_ticket_values)
  my_ticket = dict( { field_name : my_ticket_values[field_indices[field_name]] for field_name in field_indices.keys() } )
  return my_ticket
assert_equals(find_my_ticket(load_file('input/16_TEST2.txt')), {'class' : 12, 'row' : 11, 'seat' : 13})

def fields_product(ticket_fields : Dict[str, int], field_prefix='departure'):
  return product([field_value for field_name, field_value in ticket_fields.items() if field_name.startswith(field_prefix)])
assert_equals(fields_product( { 'departure time' : 4, 'schedule' : 7, 'departure platform' : 5, 'departure something' : 3}), 4*5*3)

print('part 1 sum error tickets:', sum(find_error_ticket_fields(load_file('input/16_INPUT.txt'))[0]))
print('part 2 product departure fields:', fields_product(find_my_ticket(load_file('input/16_INPUT.txt'))))
# https://adventofcode.com/2020/day/13
from typing import List
from timeit import default_timer as timer
from functools import reduce
from datetime import datetime

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def product(numbers : List[int]):     return reduce((lambda x, y: x * y), numbers)
def print_time():                     print("time:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def earliest_departure_product(lines : List[str], is_part1=True, start_at=0) -> int:
  start_timestamp, bus_ids = int(lines[0]), lines[1].split(',')
  timestamp = start_timestamp if is_part1 else start_at
  if is_part1:
    bus_ids = filter(lambda item : item != 'x', bus_ids)
    bus_ids = list(map(int, bus_ids))
  start_timer = timer()
  def all_match(timestamp : int, bus_ids : List[str], i : int, last_match : int):
    if i >= len(bus_ids): return True, None
    if bus_ids[i] != 'x':
      if not timestamp % int(bus_ids[i]) == (0 if i == 0 else int(bus_ids[i])-i): return False, last_match
      if i > 0: last_match = bus_ids[i]
    return all_match(timestamp, bus_ids, i+1, last_match) # tail recursion
  if not is_part1:
    print("input:", lines[1])
  last_printed_timestamp = timestamp
  while True:
    if is_part1:
      for bus_id in bus_ids:
        if timestamp % bus_id == 0:
          return (timestamp - start_timestamp) * bus_id
      timestamp += 1
    else:
      # part 2
      is_match, last_match = all_match(timestamp, bus_ids, i = 0, last_match=None)
      if is_match:
      # if all_match(timestamp, bus_ids, i = len(bus_ids)-1):
      # if (timestamp % 7 == 0 and timestamp % 13 == (13-1) and timestamp % 59 == (59-4) and timestamp % 31 == 31-6 and timestamp % 19 == 19-7):
        print(' found t={} in {:.2f}s, buses: {}'.format(timestamp, timer(), lines[1]))
        return timestamp
      # if False:
      if last_match:
        matching_index = bus_ids.index(last_match)
        buses = list(filter(lambda bus : bus != 'x', bus_ids[0:matching_index+1]))
        # buses = bus_ids[0:matching_index+1]
        # delta_t = max(map(int, buses)) - 1
        # delta_t = max(map(int, buses)) - 1
        delta_t = product(map(int, buses))
        # delta_t = min(map(int, filter(lambda bus : bus != 'x', buses)))
        # print(' progress match @ t={} buses -> {}, delta +{}, prior -{}'.format(timestamp, bus_ids[0:matching_index+1], delta_t, timestamp - last_printed_timestamp ))
        # if matching_index > 13: 
        # if True:
          # print('t={}, last_match(i={}) -> {} aka {}-> delta: +{}'.format(timestamp, matching_index, buses, bus_ids[0:matching_index+1], delta_t))
          # print("good progress, matching_index={}/{}, timestamp={} (len={})".format(matching_index, len(bus_ids), timestamp, len(str(timestamp))))
        last_printed_timestamp = timestamp
        timestamp += delta_t - len(buses) 
      else:
        timestamp += 1
      if timestamp % 1_000_000 == 0: print('t={} (len={})'.format(timestamp, len(str(timestamp))))

assert_equals(earliest_departure_product(['939','7,13,x,x,59,x,31,19']), 295)
assert_equals(earliest_departure_product(['000','17,x,13,19'], is_part1=False), 3417)
assert_equals(earliest_departure_product(['000','67,7,59,61'], is_part1=False), 754_018)
assert_equals(earliest_departure_product(['000','67,x,7,59,61'], is_part1=False), 779_210)
assert_equals(earliest_departure_product(['939','7,13,x,x,59,x,31,19'], is_part1=False), 1_068_781)
assert_equals(earliest_departure_product(['000','67,7,x,59,61'], is_part1=False), 1_261_476)
assert_equals(earliest_departure_product(['000','1789,37,47,1889'], is_part1=False), 1_202_161_486)
# exit()
print_time()
print('part 1: ', earliest_departure_product(load_file('input/13_INPUT.txt')))
print_time()
print('part 2: ', earliest_departure_product(load_file('input/13_INPUT.txt'), is_part1=False, start_at=100000000000000))
print_time()
# https://adventofcode.com/2020/day/15
from typing import List, Dict
from collections import defaultdict
from pyutil.testing import assert_equals

def spoken_numbers(starting_numbers : List[int], n : int = 2020):
  last_spoken_turns :  Dict[int,List[int]] = defaultdict(list) # TODO much better to use a ring buffer of length 2 here
  first_spoken_turns : Dict[int, int] = dict()
  spoken_nums = []
  i = 0 
  while len(spoken_nums) < n:
    turn = i + 1 
    is_starting_number = i < len(starting_numbers)
    # print('i={}'.format(i))
    last_spoken_num = starting_numbers[i] if is_starting_number else spoken_nums[-1]
    is_new = is_starting_number or not spoken_nums[-1] in first_spoken_turns
    if is_new:
      first_spoken_turns[last_spoken_num] = turn
      current_spoken = last_spoken_num if is_starting_number else 0
      # print('turn={} last: {} is new, spoken: {}'.format(turn, last_spoken_num, current_spoken))
    else: # is repeated
      if first_spoken_turns[last_spoken_num] == turn - 1:
        current_spoken = 0
      else:
        current_spoken = last_spoken_turns[last_spoken_num][-1] - last_spoken_turns[last_spoken_num][-2]
      # print('turn={} last: {} repeat last seen turns: {}, spoken: {}'.format(turn, last_spoken_num, last_spoken_turns[last_spoken_num], current_spoken))
    spoken_nums.append(current_spoken)
    last_spoken_turns[current_spoken].append(turn)
    i += 1
  return spoken_nums
assert_equals(spoken_numbers([0,3,6], n=10), [0,3,6,0,3,3,1,0,4,0])
assert_equals(spoken_numbers([0,3,6])[-1], 436)

print('part 1: #2020 spoken number:', spoken_numbers([1,17,0,10,18,11,6], n=2020)[-1])
print('part 2: #30M spoken number:', spoken_numbers([1,17,0,10,18,11,6], n=30000000)[-1])

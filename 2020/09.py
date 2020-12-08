# https://adventofcode.com/2020/day/8
from typing import Dict, List, Tuple

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

# functions


lines = [line for line in map(str.rstrip, open('input/09_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/08_TEST.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))

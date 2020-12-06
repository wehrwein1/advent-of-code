# https://adventofcode.com/2020/day/7
import string
from typing import List

def lines_grouped(filename) -> List[List[str]]: 
  return list(map(lambda group : group.split('\n'), open(filename).read().split('\n\n'))) # empty line indicates new group

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

# functions

lines = [line for line in map(str.rstrip, open('input/07_INPUT.txt'))]
lines = [line for line in map(str.rstrip, open('input/07_TEST.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))
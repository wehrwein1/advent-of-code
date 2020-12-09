# https://adventofcode.com/2020/day/10
from typing import List

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

def load_file(filename): 
  return [line for line in map(str.rstrip, open(filename))]



lines = load_file('input/10_INPUT.txt'); #print('\ninput (len={}): {}'.format(len(lines), lines))
lines = load_file('input/10_test.txt'); #print('\ninput (len={}): {}'.format(len(lines), lines))
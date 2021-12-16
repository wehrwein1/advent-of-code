# https://adventofcode.com/2015/day/5
from collections import Counter
import re
from pyutil.testing import assert_equals
from pyutil.fileio import file_lines

def is_nice(text : str) -> bool:
  NAUGHTY_SUBSTRINGS = ['ab', 'cd', 'pq', 'xy']
  if any(map(lambda substring : substring in text, NAUGHTY_SUBSTRINGS)):
    return False
  VOWELS = ['a','e','i','o','u']
  if sum([text.count(char) for char in VOWELS]) < 3:
    return False
  return bool(re.compile(r'(.)\1').search(text)) # 2 or more repeated chars

assert_equals(is_nice('ugknbfddgicrmopn'), True)
assert_equals(is_nice('aaa'), True)
assert_equals(is_nice('jchzalrnumimnmhp'), False)
assert_equals(is_nice('haegwjzuvuyypxyu'), False)
assert_equals(is_nice('dvszwmarrgswjxmb'), False)

print(f"Part 1: count of nice strings: {Counter(map(is_nice, file_lines('2015/input/05_INPUT.txt')))[True]}")
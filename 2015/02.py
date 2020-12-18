# https://adventofcode.com/2015/day/2
from typing import List, Tuple

def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

def compute_area_and_ribbon(lines : List[int]) -> Tuple[int, int]:
  area = 0
  ribbon = 0
  for line in lines:
    l, w, h = map(int, line.split('x'))
    area_of_smallest_side = min([l*w, l*h, w*h])
    area += 2*l*w + 2*w*h + 2*h*l + area_of_smallest_side
    ribbon += sum(sorted([l, w, h])[:2])*2 + l*w*h
  return area, ribbon
assert_equals(compute_area_and_ribbon(['2x3x4']), (58, 34))
assert_equals(compute_area_and_ribbon(['1x1x10']), (43, 14))

area, ribbon = compute_area_and_ribbon(load_file('input/02_INPUT.txt'))
print('part 1: square feet of wrapping paper:', area)
print('part 2: feet of ribbon:', ribbon)
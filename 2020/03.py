from typing import List, Tuple
from functools import reduce

# https://adventofcode.com/2020/day/3
lines = [line for line in map(str.rstrip, open('input/03_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/03_TEST.txt'))]
print('input (len={}): {}'.format(len(lines), lines))
line_count = len(lines)
line_width = len(lines[0])
print('line count:', line_count)
print('line width:', line_width)

def trees_count_on_path(lines : List[str], trajectory : Tuple[int, int]) -> int:
  inc_right, inc_down = trajectory
  position_right, position_down = 0, 0
  trees_count : int = 0
  while position_down < line_count:
    geography = lines[position_down][position_right % line_width]
    is_tree = geography == '#'
    # print('pos({},{})={}'.format(position_down, position_right, geography))
    if is_tree: trees_count += 1
    position_down += inc_down
    position_right += inc_right
  return trees_count

slopes = []
for trajectory in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
  trees_count = trees_count_on_path(lines, trajectory)
  print("trajectory(right,down)={}, trees_count={}".format(trajectory, trees_count))
  slopes.append(trees_count)

print("multiplied together:", reduce((lambda x, y: x * y), slopes))

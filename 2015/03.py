# https://adventofcode.com/2015/day/3
from typing import Dict, Tuple
from collections import defaultdict

def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

def compute_deliveries(directions : str, is_part1=True) -> Dict[Tuple[int, int], int]:
  if not is_part1:
    santa_steps = ''.join([direction for i, direction in enumerate(directions) if i % 2 == 0])
    robo_steps =  ''.join([direction for i, direction in enumerate(directions) if i % 2 == 1])
    deliveries = { **compute_deliveries(santa_steps), **compute_deliveries(robo_steps) }
  else: 
    deliveries : Dict[Tuple[int, int], int] = defaultdict(int)
    x, y = 0, 0
    deliveries[(x,y)] += 1
    for direction in directions:
      if direction == '>': x += 1
      if direction == '^': y += 1
      if direction == 'v': y -= 1
      if direction == '<': x -= 1
      deliveries[(x,y)] += 1
  return { k : deliveries[k] for k in sorted(deliveries.keys()) }
assert_equals(compute_deliveries('>'),          {(0,0): 1, (1,0): 1})
assert_equals(compute_deliveries('^>v<'),       {(0,0): 2, (0,1): 1, (1,1): 1, (1,0): 1})
assert_equals(compute_deliveries('^v^v^v^v^v'), {(0,0): 6, (0,1): 5})

assert_equals(compute_deliveries('^v', is_part1=False),         {(0,-1): 1, (0 ,0): 1, (0, 1): 1})
assert_equals(compute_deliveries('^>v<', is_part1=False),       {(0, 0): 2, (0, 1): 1, (1, 0): 1})
assert_equals(compute_deliveries('^v^v^v^v^v', is_part1=False), {(0, -5): 1, (0, -4): 1, (0, -3): 1, (0, -2): 1, (0, -1): 1, (0, 0): 1, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1})

print('part 1: houses receiving 1+ present (santa):', len(compute_deliveries(load_file('input/03_INPUT.txt')[0])))
print('part 1: houses receiving 1+ present (santa + robo):', len(compute_deliveries(load_file('input/03_INPUT.txt')[0], is_part1=False)))
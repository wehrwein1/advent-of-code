# https://adventofcode.com/2020/day/24
from typing import List, Dict, Tuple
from collections import defaultdict

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]

def parse_instructions(line: str) -> List[str]:
  instructions = []
  i = 0
  while i < len(line):
    next_instruction = line[i]
    if not next_instruction in ['e','w']:
      next_instruction = line[i:i+2]
    instructions += [next_instruction]
    i += len(next_instruction)
  return instructions
assert_equals(parse_instructions('esew'), ['e','se','w'])
assert_equals(parse_instructions('nwwswee'), ['nw','w','sw','e','e'])
assert_equals(parse_instructions('sesenwnenenewseeswwswswwnenewsewsw'), ['se','se','nw','ne','ne','ne','w','se','e','sw','w','sw','sw','w','ne','ne','w','se','w','sw'])

WHITE : int = 0
BLACK : int = 1
def compute_flipped_tiles(lines : List[str]):
  position_counts = defaultdict(int)
  for line in lines:
    (x,y,z) = 0,0,0
    for instr in parse_instructions(line):
      if instr == 'ne': x += 1; z -= 1
      if instr == 'e':  x += 1; y -= 1
      if instr == 'se': y -= 1; z += 1
      if instr == 'sw': x -= 1; z += 1
      if instr == 'w':  x -= 1; y += 1
      if instr == 'nw': y += 1; z -= 1
    position_counts[(x,y,z)] += 1
  return position_counts
assert_equals(compute_flipped_tiles(['esew']), { (0,-1,1): 1 })
assert_equals(compute_flipped_tiles(['nwwswee']), {(0,0,0) :1})

def count_black(position_counts : Dict[Tuple[int,int], int]) -> int:
  return len( {tile:flip_count for tile,flip_count in position_counts.items() if flip_count % 2 == BLACK} )
assert_equals(count_black( { (0,0): 1, (0,-1): 2, (1,2): 5} ), 2)

# part 1
assert_equals(compute_flipped_tiles(load_file('2020/input/24_TEST.txt')), {(-3, 1, 2): 1, (1, 2, -3): 2, (-3, 0, 3): 1, (2, 0, -2): 2, (1, 1, -2): 2, (-1, 1, 0): 2, (-2, 2, 0): 1, (0, 1, -1): 1, (-2, 1, 1): 1, (0, 2, -2): 2, (3, 0, -3): 1, (0, -2, 2): 1, (0, 0, 0): 1, (2, -2, 0): 1, (-1, 2, -1): 1})
assert_equals(count_black(compute_flipped_tiles(load_file('2020/input/24_TEST.txt'))), 10)
print(f"part 1: number of tiles flipped to black: {count_black(compute_flipped_tiles(load_file('2020/input/24_INPUT.txt')))}")
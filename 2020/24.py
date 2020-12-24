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

hexagonal_directions = {        # x,  y,  z
                          'ne' : (1,  0, -1),
                          'e'  : (1, -1,  0),
                          'se' : (0, -1,  1),
                          'sw' : (-1, 0,  1),
                          'w'  : (-1, 1,  0),
                          'nw' : (0,  1, -1) }
WHITE : int = 0 # default when unset, defaultdict
BLACK : int = 1
def flip_tiles(lines : List[str], position_counts = None): 
  # I learned something - these default param values are created *once* and persisted across calls
  # see https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
  if position_counts is None: 
    position_counts = defaultdict(int)
  for line in lines:
    (x,y,z) = 0,0,0
    for instr in parse_instructions(line):
      delta_x, delta_y, delta_z = hexagonal_directions[instr]
      x += delta_x
      y += delta_y
      z += delta_z
    position_counts[(x,y,z)] += 1 # flip this position
  return position_counts
assert_equals(flip_tiles(['esew']),    {(0,-1,1): 1})
assert_equals(flip_tiles(['nwwswee']), {(0,0,0) : 1})

def get_tiles(position_counts : Dict[Tuple[int,int,int], int], desired_color) -> Dict[Tuple[int,int,int],int]:
  return {tile:flip_count for tile,flip_count in position_counts.items() if flip_count % 2 == desired_color}
assert_equals(get_tiles( { (0,0): 1, (0,-1): 2, (1,2): 5}, desired_color=BLACK), {(0, 0): 1, (1, 2): 5})
assert_equals(get_tiles( { (0,0): 1, (0,-1): 2, (1,2): 5}, desired_color=WHITE), {(0, -1): 2})

def tile_count(position_counts : Dict[Tuple[int,int,int], int], desired_color) -> int:
  return len( get_tiles(position_counts, desired_color=desired_color))
assert_equals(tile_count( { (0,0): 1, (0,-1): 2, (1,2): 5}, desired_color=BLACK), 2)

def get_all_adjacent_tiles(position_counts : Dict[Tuple[int,int], int], origin_tile) -> Dict[Tuple[int,int], int]:
  adjacent_tiles = {}
  for direction, (delta_x, delta_y, delta_z) in hexagonal_directions.items():
    new_x, new_y, new_z = origin_tile
    new_x += delta_x
    new_y += delta_y
    new_z += delta_z
    adjacent_tile = (new_x, new_y, new_z)
    if adjacent_tile in position_counts: 
      adjacent_tiles[adjacent_tile] = position_counts[adjacent_tile]
  return adjacent_tiles

def simulate_art_exhibit(lines : List[str], num_days=100):
  black_tile_counts = []
  position_counts = defaultdict(int)
  for i in range(num_days):
    position_counts = flip_tiles(lines, position_counts=position_counts)
    black_tiles = get_tiles(position_counts, desired_color=BLACK)
    white_tiles = get_tiles(position_counts, desired_color=WHITE)
    assert set(black_tiles).intersection(set(white_tiles)) == set(), 'Black and white tiles overlap??'
    tiles_to_flip = set()
    for black_tile in black_tiles:
      adjacent_tiles = get_all_adjacent_tiles(position_counts, black_tile)
      adjacent_black_tiles_count = tile_count(adjacent_tiles, desired_color=BLACK)
      is_flip = adjacent_black_tiles_count == 0 or adjacent_black_tiles_count > 2
      if is_flip: tiles_to_flip.add(black_tile)
    for white_tile in white_tiles:
      adjacent_tiles = get_all_adjacent_tiles(position_counts, white_tile)
      adjacent_black_tiles_count = tile_count(adjacent_tiles, desired_color=BLACK)
      is_flip = adjacent_black_tiles_count == 2
      if is_flip: tiles_to_flip.add(white_tile)
    for tile in tiles_to_flip:
      position_counts[tile] += 1 # flips both black and white
    black_tile_count = tile_count(position_counts, desired_color=BLACK)
    print(f"Day {i+1}: flipped {len(tiles_to_flip)}, black: {len(black_tiles)}->{black_tile_count}, white: {len(white_tiles)}->{tile_count(position_counts, desired_color=WHITE)}")
    black_tile_counts += [black_tile_count]
  return black_tile_counts
# part 2
assert_equals(simulate_art_exhibit(load_file('2020/input/24_TEST.txt'), num_days=10), [15,12,25,14,23,28,41,37,49,37])
assert_equals(simulate_art_exhibit(load_file('2020/input/24_TEST.txt'), num_days=100)[-1], 2208)

# part 1
assert_equals(flip_tiles(load_file('2020/input/24_TEST.txt')), {(-3, 1, 2): 1, (1, 2, -3): 2, (-3, 0, 3): 1, (2, 0, -2): 2, (1, 1, -2): 2, (-1, 1, 0): 2, (-2, 2, 0): 1, (0, 1, -1): 1, (-2, 1, 1): 1, (0, 2, -2): 2, (3, 0, -3): 1, (0, -2, 2): 1, (0, 0, 0): 1, (2, -2, 0): 1, (-1, 2, -1): 1})
assert_equals(tile_count(flip_tiles(load_file('2020/input/24_TEST.txt')), desired_color=BLACK), 10)
print(f"part 1: number of tiles flipped to black: {tile_count(flip_tiles(load_file('2020/input/24_INPUT.txt')), desired_color=BLACK)}")

# part 2
print(f"part 2: number of tiles flipped to black: {simulate_art_exhibit(load_file('2020/input/24_INPUT.txt'))[-1]}") # tried 187
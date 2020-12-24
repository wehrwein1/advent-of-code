# https://adventofcode.com/2020/day/24
from typing import List, Dict, Tuple, Set
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
def flip_tiles(lines : List[str], position_counts = None) -> Dict[Tuple[int,int,int], int]: 
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

def get_tiles(position_counts : Dict[Tuple[int,int,int], int], desired_color) -> Set[Tuple[int,int,int]]:
  return set( tile for tile, flip_count in position_counts.items() if flip_count % 2 == desired_color )
assert_equals(sorted(get_tiles( { (0,0): 1, (0,-1): 2, (1,2): 5}, BLACK)), [(0, 0), (1, 2)])
assert_equals(get_tiles( { (0,0): 1, (0,-1): 2, (1,2): 5}, WHITE), {(0,-1)})

def count_tiles(position_counts : Dict[Tuple[int,int,int], int], desired_color) -> int:
  return len( get_tiles(position_counts, desired_color=desired_color))
assert_equals(count_tiles( { (0,0): 1, (0,-1): 2, (1,2): 5}, desired_color=BLACK), 2)

def compute_neighbors(origin_tile) -> List[Tuple[int,int,int]]:
  return [ 
    (origin_tile[0] + delta_x, 
     origin_tile[1] + delta_y, 
     origin_tile[2] + delta_z) for direction, (delta_x, delta_y, delta_z) in hexagonal_directions.items() ]
assert_equals(compute_neighbors((0,0,0)), [(1, 0, -1), (1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1)])
assert_equals(compute_neighbors((2,5,8)), [(3, 5, 7), (3, 4, 8), (2, 4, 9), (1, 5, 9), (1, 6, 8), (2, 6, 7)])

def simulate_art_exhibit(lines : List[str], num_days=100):
  black_tile_counts = []
  position_counts = flip_tiles(lines) # state change
  for _ in range(num_days):
    black_tiles = get_tiles(position_counts, BLACK)
    white_tiles = get_tiles(position_counts, WHITE)
    tiles_to_flip = set()
    for black_tile in black_tiles:
      neighbors = compute_neighbors(black_tile)
      blacks = list(filter(lambda tile : position_counts[tile] % 2 == BLACK, neighbors))
      if len(blacks) == 0 or len(blacks) > 2: tiles_to_flip.add(black_tile)
      new_whites = set(filter(lambda tile : position_counts[tile] % 2 == WHITE, neighbors))
      white_tiles.update(new_whites)
    for white_tile in white_tiles:
      neighbors = compute_neighbors(white_tile)
      blacks = list(filter(lambda tile : position_counts[tile] % 2 == BLACK, neighbors))
      if len(blacks) == 2: tiles_to_flip.add(white_tile)
    for tile in tiles_to_flip:
      position_counts[tile] += 1 # flips both black and white, state change
    black_tile_counts += [count_tiles(position_counts, BLACK)]
  return black_tile_counts
# part 2
assert_equals(simulate_art_exhibit(load_file('2020/input/24_TEST.txt'), num_days=1), [15])
assert_equals(simulate_art_exhibit(load_file('2020/input/24_TEST.txt'), num_days=10), [15,12,25,14,23,28,41,37,49,37])
assert_equals(simulate_art_exhibit(load_file('2020/input/24_TEST.txt'), num_days=100)[-1], 2208)

# part 1
assert_equals(flip_tiles(load_file('2020/input/24_TEST.txt')), {(-3, 1, 2): 1, (1, 2, -3): 2, (-3, 0, 3): 1, (2, 0, -2): 2, (1, 1, -2): 2, (-1, 1, 0): 2, (-2, 2, 0): 1, (0, 1, -1): 1, (-2, 1, 1): 1, (0, 2, -2): 2, (3, 0, -3): 1, (0, -2, 2): 1, (0, 0, 0): 1, (2, -2, 0): 1, (-1, 2, -1): 1})
assert_equals(count_tiles(flip_tiles(load_file('2020/input/24_TEST.txt')), desired_color=BLACK), 10)
assert_equals(count_tiles(flip_tiles(load_file('2020/input/24_TEST.txt')), desired_color=WHITE), 5)
print(f"part 1: number of tiles flipped to black: {count_tiles(flip_tiles(load_file('2020/input/24_INPUT.txt')), desired_color=BLACK)}")
# part 2
print(f"part 2: number of tiles flipped to black: {simulate_art_exhibit(load_file('2020/input/24_INPUT.txt'))[-1]}") 
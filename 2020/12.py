# https://adventofcode.com/2020/day/11
from typing import List

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]

cardinal_direction_vectors = dict( { 'N' : (0, 1), 
                                     'E' : (1, 0),
                                     'S' : (0,-1),
                                     'W' : (-1,0) })

def get_direction(current_cardinal_dir : str, action : str, rotation_value=None) -> str:
  if action == 'F': return current_cardinal_dir # direction unchanged
  assert not rotation_value is None and rotation_value > 0 and rotation_value < 360, "invalid rotation value: " + str(rotation_value)
  cardinal_directions = list(cardinal_direction_vectors.keys())
  if action == 'L': rotation_value = (360 - rotation_value) # convert to clockwise 
  index = cardinal_directions.index(current_cardinal_dir) + int(rotation_value / 90)
  return cardinal_directions[index % len(cardinal_directions)]
assert_equals(get_direction(current_cardinal_dir="E", action="F"), "E") # direction unchanged
assert_equals(get_direction(current_cardinal_dir="E", action="R", rotation_value=180), "W") 
assert_equals(get_direction(current_cardinal_dir="E", action="R", rotation_value=270), "N") 
assert_equals(get_direction(current_cardinal_dir="S", action="R", rotation_value=270), "E") 
assert_equals(get_direction(current_cardinal_dir="N", action="R", rotation_value=90),  "E")
assert_equals(get_direction(current_cardinal_dir="E", action="L", rotation_value=270), "S")

def move(x : int, y : int, facing_cardinal_dir : str, move_instruction : str):
  action, value = move_instruction[0], int(move_instruction[1:])
  instruction_cardinal_dir = action if action in cardinal_direction_vectors else get_direction(facing_cardinal_dir, action, rotation_value=value)
  if action in ['R','L']: # rotate
    return x, y, instruction_cardinal_dir # rotate changes directly only
  delta_x, delta_y = map(lambda pos : pos * value, cardinal_direction_vectors[instruction_cardinal_dir])
  x, y = x + delta_x, y + delta_y
  return x, y, facing_cardinal_dir
assert_equals(move(0,0,  "E", "F10"),  (10,0, "E"))
assert_equals(move(10,0, "E", "N3"),   (10,3, "E"))
assert_equals(move(10,3, "E", "F7"),   (17,3, "E"))
assert_equals(move(17,3, "E", "R90"),  (17,3, "S"))
assert_equals(move(10,5, "E", "L270"), (10,5, "S"))

def compute_manhattan_distance(instructions : List[str]):
  (x,y) = (0,0)
  facing_direction = "E"
  for i, instruction in enumerate(instructions):
    new_x, new_y, new_dir = move(x, y, facing_direction, instruction)
    print('{}: {} facing {} -> "{}" -> {} facing {}'.format(i, (x,y), facing_direction, instruction, (new_x, new_y), new_dir))
    x, y, facing_direction = new_x, new_y, new_dir
  # print('final location:', (x, y))
  return sum(map(abs, (x,y)))
assert_equals(compute_manhattan_distance(load_file('input/12_TEST.txt')), 25)

print('part1 manhattan distance: ', compute_manhattan_distance(load_file('input/12_INPUT.txt')))

# https://adventofcode.com/2020/day/12
from typing import List
from pyutil.testing import assert_equals
from pyutil.fileio import file_lines
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

def compute_deltas(facing_cardinal_dir : str, move_instruction : str):
  action, value = move_instruction[0], int(move_instruction[1:])
  instruction_cardinal_dir = action if action in cardinal_direction_vectors else get_direction(facing_cardinal_dir, action, rotation_value=value)
  if action in ['R','L']: # rotate
    return 0, 0, instruction_cardinal_dir # rotate changes directly only
  delta_x, delta_y = map(lambda pos : pos * value, cardinal_direction_vectors[instruction_cardinal_dir])
  return delta_x, delta_y, facing_cardinal_dir
assert_equals(compute_deltas("E", "F10"),  (10,0, "E"))
assert_equals(compute_deltas("E", "N3"),   (0,3, "E"))
assert_equals(compute_deltas("E", "F7"),   (7,0, "E"))
assert_equals(compute_deltas("E", "R90"),  (0,0, "S"))
assert_equals(compute_deltas("E", "L270"), (0,0, "S"))
assert_equals(compute_deltas("E", "F10"),  (10,0, "E"))

def rotate_right(x, y, degrees):
  if degrees == 90:  return y, -x
  if degrees == 180: return -x, -y
  if degrees == 270: return -y, x

def compute_manhattan_distance(instructions : List[str], is_part1=True):
  (x,y) = (0,0)
  facing_direction = "E"
  waypoint_x, waypoint_y = (10, 1)
  for i, instruction in enumerate(instructions):
    if is_part1:
      delta_x, delta_y, new_dir = compute_deltas(facing_direction, instruction)
      new_x, new_y, = x + delta_x, y + delta_y
      print('{}: {} facing {} -> "{}" -> ship {} facing {}'.format(i, (x,y), facing_direction, instruction, (new_x, new_y), new_dir))
      (x, y, facing_direction) = new_x, new_y, new_dir
    else:
      action, value = instruction[0], int(instruction[1:])
      if action == 'F': # move ship, interpret as * waypoint
        delta_x, delta_y = map(lambda x : x * value, [waypoint_x, waypoint_y])
        new_dir = facing_direction
        new_x, new_y, = x + delta_x, y + delta_y
        print('{}: {} facing {} -> "{}" -> (deltas: {}) -> ship {} facing {}, waypoint: {}'.format(i, (x,y), facing_direction, instruction, (delta_x, delta_y), (new_x, new_y), new_dir, (waypoint_x, waypoint_y)))
        (x, y, facing_direction) = new_x, new_y, new_dir
      else: # move waypoint
        delta_x, delta_y, new_dir = compute_deltas(facing_direction, instruction)
        if action in ['L','R']:
          delta_x, delta_y = cardinal_direction_vectors[new_dir]
          if action == 'L':
            value = 360 - value # convert to right
            action = 'R'
          waypoint_x, waypoint_y = rotate_right(waypoint_x, waypoint_y, value)
          print('{}: {} facing {} -> "{}" -> (waypoint proj deltas: {}) -> facing {}, waypoint: {}'.format(i, (x,y), facing_direction, instruction, (delta_x, delta_y), new_dir, (waypoint_x, waypoint_y)))
        else:
          waypoint_x, waypoint_y = waypoint_x + delta_x, waypoint_y + delta_y
          print('{}: {} facing {} -> "{}" -> (waypoint deltas: {}) -> facing {}, waypoint: {}'.format(i, (x,y), facing_direction, instruction, (delta_x, delta_y), new_dir, (waypoint_x, waypoint_y)))
        facing_direction = new_dir
  # print('final location:', (x, y))
  return sum(map(abs, (x,y)))
assert_equals(compute_manhattan_distance(file_lines('2020/input/12_TEST.txt')), 25)
assert_equals(compute_manhattan_distance(file_lines('2020/input/12_TEST.txt'), is_part1=False), 286)

print('part1 manhattan distance: ', compute_manhattan_distance(file_lines('2020/input/12_INPUT.txt')))
print('part2 manhattan distance: ', compute_manhattan_distance(file_lines('2020/input/12_INPUT.txt'), is_part1=False))
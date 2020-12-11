# https://adventofcode.com/2020/day/11
from typing import List, Dict
from collections import Counter
from functools import reduce

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]

seat_occupied =   '#'
seat_empty =      'L'

def count_seats_nearby(seating_area : List[str], row, col) -> Dict[str,int]:
  num_rows = len(seating_area)
  num_cols = len(seating_area[0])
  # print("input: num_rows: {}, num_cols: {}".format(num_rows, num_cols))
  row_bounds = (row - 1 if row > 0 else 0), (row + 1 if row < num_rows - 1 else num_rows - 1)
  col_bounds = (col - 1 if col > 0 else 0), (col + 1 if col < num_cols - 1 else num_cols - 1)
  # print('seat: row={}, col={}, row_bounds={}, col_bounds={}'.format(row, col, row_bounds, col_bounds))
  nearby_seats = [seating_area[i][col_bounds[0]:col_bounds[1]+1] for i in range(row_bounds[0], row_bounds[1]+1)]
  # print('nearby_seats:', '\n' + '\n'.join(nearby_seats))
  return dict( (seat_char, sum([1 for seat in ''.join(nearby_seats) if seat == seat_char]) + (-1 if seating_area[row][col] == seat_char else 0)) for seat_char in ['#','L','.'])
assert_equals(count_seats_nearby(load_file('input/11_TEST.txt'), row=1, col=1), {'#': 0, 'L': 6, '.' : 2})
assert_equals(count_seats_nearby(load_file('input/11_TEST.txt'), row=0, col=1), {'#': 0, 'L': 5, '.' : 0})
assert_equals(count_seats_nearby(load_file('input/11_TEST.txt'), row=6, col=7), {'#': 0, 'L': 5, '.' : 3})
assert_equals(count_seats_nearby(load_file('input/11_TEST.txt'), row=8, col=9), {'#': 0, 'L': 4, '.' : 1})

def simulate(seating_area : List[str]) -> List[str]:
  num_rows = len(seating_area)
  num_cols = len(seating_area[0])
  next_state = [row for row in seating_area]
  for row in range(0, num_rows):
    new_row = []
    for col in range(0, num_cols):
      seat = seating_area[row][col]
      nearby_seats = count_seats_nearby(seating_area, row, col)
      new_seat = seat
      if seat == seat_empty and nearby_seats[seat_occupied] == 0:
        new_seat = seat_occupied
      elif seat == seat_occupied and nearby_seats[seat_occupied] >= 4:
        new_seat = seat_empty
      new_row += [new_seat]
    # print('new_row[{}]={}'.format(row, ''.join(new_row)))
    next_state[row] = ''.join(new_row)
  return next_state

test_data_rounds = [
  ['#.##.##.##','#######.##','#.#.#..#..','####.##.##','#.##.##.##','#.#####.##','..#.#.....','##########','#.######.#','#.#####.##'], # "After one round of these rules.."
  ['#.LL.L#.##','#LLLLLL.L#','L.L.L..L..','#LLL.LL.L#','#.LL.LL.LL','#.LLLL#.##','..L.L.....','#LLLLLLLL#','#.LLLLLL.L','#.#LLLL.##'], # "After a second round.."
  ['#.##.L#.##','#L###LL.L#','L.#.#..#..','#L##.##.L#','#.##.LL.LL','#.###L#.##','..#.#.....','#L######L#','#.LL###L.L','#.#L###.##'], # "process coninues for three more.." (1)
  ['#.#L.L#.##','#LLL#LL.L#','L.L.L..#..','#LLL.##.L#','#.LL.LL.LL','#.LL#L#.##','..L.L.....','#L#LLLL#L#','#.LLLLLL.L','#.#L#L#.##'], # (2)
  ['#.#L.L#.##','#LLL#LL.L#','L.#.L..#..','#L##.##.L#','#.#L.LL.LL','#.#L#L#.##','..L.L.....','#L#L##L#L#','#.LLLLLL.L','#.#L#L#.##']  # (3)
]

assert_equals(simulate(load_file('input/11_TEST.txt')), test_data_rounds[0])
assert_equals(simulate(test_data_rounds[0]), test_data_rounds[1])
assert_equals(simulate(test_data_rounds[1]), test_data_rounds[2])
assert_equals(simulate(test_data_rounds[2]), test_data_rounds[3])
assert_equals(simulate(test_data_rounds[3]), test_data_rounds[4])

def simulate_until_stable(seating_area : List[str]) -> List[str]:
  last_state = None
  current_state = seating_area
  while current_state != last_state:
    last_state = current_state
    current_state = simulate(current_state)
  return current_state

def count_seats_stable(seating_area):
  stable_seats = simulate_until_stable(seating_area)
  # for i, row in enumerate(stable_seats):
    # print("stable[{}]={}".format(i, row))
  all_seats = ''.join(stable_seats)
  return Counter(all_seats)
assert_equals(count_seats_stable(load_file('input/11_TEST.txt')), {'#': 37, 'L': 34, '.': 29})

print('part 1: count occupied seats:', count_seats_stable(load_file('input/11_INPUT.txt'))[seat_occupied])
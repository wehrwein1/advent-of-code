# https://adventofcode.com/2020/day/11
from typing import List, Dict
from collections import Counter
from pyutil.fileio import file_lines
from pyutil.testing import assert_equals

def set_char(text : str, i : int, one_char : str): # Note: O(n), eek
  buffer = list(''.join(text))
  buffer[i:i+1] = one_char
  return ''.join(buffer)
assert_equals(set_char('abc', 1, '_'), 'a_c')
assert_equals(set_char('abc', 2, 'x'), 'abx')

seat_occupied =   '#'
seat_empty =      'L'
seat_floor =      '.'

def count_seats_nearby(seating_area : List[str], row, col, is_part1=True) -> Dict[str,int]:
  num_rows = len(seating_area)
  num_cols = len(seating_area[0])
  active_seat = seating_area[row][col]
  seating_area[row] = set_char(seating_area[row], col, '*')
  if not is_part1:
    seat_unset        = '?'
    seat_none_found   = '_'
    nearby_seats : List[str] = [seat_unset] * 8
    # occupied_count = 0
    for i, (rowdir, coldir) in enumerate([(-1,-1), (-1,0), (-1,1), 
                                          (0, -1),         (0, 1), 
                                          (1, -1), (1, 0), (1, 1)]):
      # print("starting from: {} ('{}') i={} along trajectory {}".format((row, col), seating_area[row][col], i, (rowdir, coldir)))
      cur_row = row 
      cur_col = col
      cur_row += rowdir
      cur_col += coldir
      cur_seat = seat_none_found
      while (cur_row >= 0 and cur_row <= num_rows - 1) and (cur_col >= 0 and cur_col <= num_cols - 1):
        # apply trajectory until we find one
        cur_seat = seating_area[cur_row][cur_col]
        # print(' trajectory along {} to {} => {}'.format( (rowdir, coldir), (cur_row, cur_col), cur_seat))
        if cur_seat != seat_floor:
          nearby_seats[i] = cur_seat
          break # resume next trajectory
        cur_row += rowdir
        cur_col += coldir
      if cur_seat == seat_none_found:
        # print("  did not find, using seat=", cur_seat)
        nearby_seats[i] = cur_seat
      # print("  nearby_seats: '{}'".format(''.join(nearby_seats)))
    nearby_seats.insert(4, '*')
    # print('nearby:')
    # print("{}".format(nearby_seats_debug[0:3]))
    # print("{}".format(nearby_seats_debug[3:6]))
    # print("{}".format(nearby_seats_debug[6:]))
  else: 
    # print("input: num_rows: {}, num_cols: {}".format(num_rows, num_cols))
    row_bounds = (row - 1 if row > 0 else 0), (row + 1 if row < num_rows - 1 else num_rows - 1)
    col_bounds = (col - 1 if col > 0 else 0), (col + 1 if col < num_cols - 1 else num_cols - 1)
  # print('seat: row={}, col={}, row_bounds={}, col_bounds={}'.format(row, col, row_bounds, col_bounds))
    nearby_seats = [seating_area[i][col_bounds[0]:col_bounds[1]+1] for i in range(row_bounds[0], row_bounds[1]+1)]
    # print('nearby_seats:', '\n' + '\n'.join(nearby_seats))
    # return dict( (seat_char, sum([1 for seat in ''.join(nearby_seats) if seat == seat_char]) + (-1 if seating_area[row][col] == seat_char else 0)) for seat_char in ['#','L','.'])
  seating_area[row] = set_char(seating_area[row], col, active_seat)
  return ''.join(nearby_seats)
assert_equals(count_seats_nearby(file_lines('2020/input/11_TEST.txt'), row=1, col=1), 'L.LL*LL.L')  # {'#': 0, 'L': 6, '.' : 2})
assert_equals(count_seats_nearby(file_lines('2020/input/11_TEST.txt'), row=0, col=1), 'L*LLLL')     # {'#': 0, 'L': 5, '.' : 0})
assert_equals(count_seats_nearby(file_lines('2020/input/11_TEST.txt'), row=6, col=7), 'L.L.*.LLL')  # {'#': 0, 'L': 5, '.' : 3})
assert_equals(count_seats_nearby(file_lines('2020/input/11_TEST.txt'), row=8, col=9), 'LL.*LL')     # {'#': 0, 'L': 4, '.' : 1})
# part 2 tests
assert_equals(count_seats_nearby(['.......#.','...#.....','.#.......','.........','..#L....#','....#....','.........','#........','...#.....'], row=4, col=3, is_part1=False), '####*####') # {'#' : 8, 's' : 1})
assert_equals(count_seats_nearby(['.##.##.','#.#.#.#','##...##','...L...','##...##','#.#.#.#','.##.##.'], row=3, col=3, is_part1=False), '????*????') # {'?' : 8, 's' : 1}) # none occuplied ('#') 

def simulate(seating_area : List[str], is_part1=True) -> List[str]:
  num_rows = len(seating_area)
  num_cols = len(seating_area[0])
  # print("in simulate()")
  # for row in seating_area:
  #   print(' input:', row)
  next_state = [row for row in seating_area]
  for row in range(0, num_rows):
    new_row = []
    for col in range(0, num_cols):
      seat = seating_area[row][col]
      nearby_seats = Counter(count_seats_nearby(seating_area, row, col, is_part1))
      new_seat = seat
      if seat == seat_empty and nearby_seats[seat_occupied] == 0:
        new_seat = seat_occupied
      elif seat == seat_occupied and nearby_seats[seat_occupied] >= (4 if is_part1 else 5):
        new_seat = seat_empty
      new_row += [new_seat]
    # print('new_row[{}]={}'.format(row, ''.join(new_row)))
    next_state[row] = ''.join(new_row)
  # print("simulate outpt: num_rows: {}, num_cols: {}".format(num_rows, num_cols))
  # if seating_area == next_state: print("WARNING: simulate() did not change input")
  return next_state

# part 1 tests
part1_simulations = [
  ['#.##.##.##','#######.##','#.#.#..#..','####.##.##','#.##.##.##','#.#####.##','..#.#.....','##########','#.######.#','#.#####.##'], # "After one round of these rules.."
  ['#.LL.L#.##','#LLLLLL.L#','L.L.L..L..','#LLL.LL.L#','#.LL.LL.LL','#.LLLL#.##','..L.L.....','#LLLLLLLL#','#.LLLLLL.L','#.#LLLL.##'], # "After a second round.."
  ['#.##.L#.##','#L###LL.L#','L.#.#..#..','#L##.##.L#','#.##.LL.LL','#.###L#.##','..#.#.....','#L######L#','#.LL###L.L','#.#L###.##'], # "process coninues for three more.." (1)
  ['#.#L.L#.##','#LLL#LL.L#','L.L.L..#..','#LLL.##.L#','#.LL.LL.LL','#.LL#L#.##','..L.L.....','#L#LLLL#L#','#.LLLLLL.L','#.#L#L#.##'], # (2)
  ['#.#L.L#.##','#LLL#LL.L#','L.#.L..#..','#L##.##.L#','#.#L.LL.LL','#.#L#L#.##','..L.L.....','#L#L##L#L#','#.LLLLLL.L','#.#L#L#.##']  # (3)
]
assert_equals(simulate(file_lines('2020/input/11_TEST.txt')), part1_simulations[0])
assert_equals(simulate(part1_simulations[0]),           part1_simulations[1])
assert_equals(simulate(part1_simulations[1]),           part1_simulations[2])
assert_equals(simulate(part1_simulations[2]),           part1_simulations[3])
assert_equals(simulate(part1_simulations[3]),           part1_simulations[4])

# part 2 tests
part2_simulations = [
  ['#.##.##.##','#######.##','#.#.#..#..','####.##.##','#.##.##.##','#.#####.##','..#.#.....','##########','#.######.#','#.#####.##'], # 0
  ['#.LL.LL.L#','#LLLLLL.LL','L.L.L..L..','LLLL.LL.LL','L.LL.LL.LL','L.LLLLL.LL','..L.L.....','LLLLLLLLL#','#.LLLLLL.L','#.LLLLL.L#'], # 1
  ['#.L#.##.L#','#L#####.LL','L.#.#..#..','##L#.##.##','#.##.#L.##','#.#####.#L','..#.#.....','LLL####LL#','#.L#####.L','#.L####.L#'], # 2
  ['#.L#.L#.L#','#LLLLLL.LL','L.L.L..#..','##LL.LL.L#','L.LL.LL.L#','#.LLLLL.LL','..L.L.....','LLLLLLLLL#','#.LLLLL#.L','#.L#LL#.L#'],
  ['#.L#.L#.L#','#LLLLLL.LL','L.L.L..#..','##L#.#L.L#','L.L#.#L.L#','#.L####.LL','..#.#.....','LLL###LLL#','#.LLLLL#.L','#.L#LL#.L#'],
  ['#.L#.L#.L#','#LLLLLL.LL','L.L.L..#..','##L#.#L.L#','L.L#.LL.L#','#.LLLL#.LL','..#.L.....','LLL###LLL#','#.LLLLL#.L','#.L#LL#.L#']
]
assert_equals(simulate(file_lines('2020/input/11_TEST.txt'), is_part1=False), part2_simulations[0])
assert_equals(simulate(part2_simulations[0],           is_part1=False), part2_simulations[1])
assert_equals(simulate(part2_simulations[1],           is_part1=False), part2_simulations[2])
assert_equals(simulate(part2_simulations[2],           is_part1=False), part2_simulations[3])
assert_equals(simulate(part2_simulations[3],           is_part1=False), part2_simulations[4])
assert_equals(simulate(part2_simulations[4],           is_part1=False), part2_simulations[5])

def simulate_until_stable(seating_area : List[str], is_part1=True) -> List[str]:
  last_state = None
  current_state = seating_area
  while current_state != last_state:
    last_state = current_state
    current_state = simulate(current_state, is_part1)
  return current_state

def count_seats_stable(seating_area, is_part1=True):
  stable_seats = simulate_until_stable(seating_area, is_part1)
  all_seats = ''.join(stable_seats)
  return Counter(all_seats)
assert_equals(count_seats_stable(file_lines('2020/input/11_TEST.txt')), {'#': 37, 'L': 34, '.': 29})
assert_equals(count_seats_stable(file_lines('2020/input/11_TEST.txt'))[seat_occupied], 37)

print('part 1: count occupied seats:', count_seats_stable(file_lines('2020/input/11_INPUT.txt'), is_part1=True)[seat_occupied])
print('part 2: count occupied seats:', count_seats_stable(file_lines('2020/input/11_INPUT.txt'), is_part1=False)[seat_occupied])
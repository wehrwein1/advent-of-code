# https://adventofcode.com/2020/day/5
from pyutil.fileio import file_lines

lines = file_lines('2020/input/05_INPUT.txt')

def compute_row(row_spec : str) -> int:
  return int(''.join(list(map(lambda char : '1' if char =='B' else '0', list(row_spec)))), 2)

def compute_col(col_spec : int) -> int:
  return int(''.join(list(map(lambda char : '1' if char =='R' else '0', list(col_spec)))), 2)

def compute_seat_id(seat_spec):
  row = compute_row(seat_spec[:7])
  col = compute_col(seat_spec[7:])
  seat_id = row*8 + col
  print(" spec={}, row={}, col={}, seat_id={}".format(seat_spec, row, col, seat_id))
  return seat_id

seat_ids = [compute_seat_id(line) for line in lines]
min_seat, max_seat = min(seat_ids), max(seat_ids)
empty_seats = [seat_id for seat_id in range(min_seat, max_seat) if not seat_id in seat_ids]
print("min_seat={}, max_seat={}, empty_seats={}".format(min_seat, max_seat, empty_seats))
# https://adventofcode.com/2020/day/5
lines = [line for line in map(str.rstrip, open('input/05_INPUT.txt'))]
# lines = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
# print('input (len={}): {}'.format(len(lines), lines))
print('input (len={})'.format(len(lines)))

def compute_row(row_spec : str) -> int:
  min_row = 0
  max_row = 127
  inc = 128
  for spec in row_spec:
    if (spec == 'F'): 
      max_row -= inc/2
    elif (spec == 'B'):
      min_row += inc/2
    else: raise SystemError('invalid row_spec', row_spec)
    inc /= 2
  return int(min_row)

def compute_col(col_spec : int) -> int:
  min_col = 0
  max_col = 7
  inc = 8
  for spec in col_spec:
    if (spec == 'R'): 
      min_col += inc/2
    elif (spec == 'L'):
      max_col -= inc/2
    else: raise SystemError('invalid col_spec', col_spec)
    inc /= 2
  return int(min_col)

seat_ids = []
for line in lines:
  # print(line)
  row = compute_row(line[:7])
  col = compute_col(line[7:])
  seat_id = row*8 + col
  print(" spec={}, row={}, col={}, seat_id={}".format(line, row, col, seat_id))
  seat_ids.append(seat_id)

min_seat = min(seat_ids)
max_seat = max(seat_ids)
print("min seat_id:", min_seat)
print("max seat_id:", max_seat)

empty_seats = [seat_id for seat_id in range(min_seat, max_seat) if not seat_id in seat_ids]
print("empty_seats:", empty_seats)
from day05 import compute_seat_id, compute_row, compute_col

def test_compute_seat_id():
  assert compute_seat_id('BFFFBBFRRR') == 567; assert compute_row('BFFFBBF') == 70;  assert compute_col('RRR') == 7
  assert compute_seat_id('FFFBBBFRRR') == 119; assert compute_row('FFFBBBF') == 14;  assert compute_col('RRR') == 7
  assert compute_seat_id('BBFFBBFRLL') == 820; assert compute_row('BBFFBBF') == 102; assert compute_col('RLL') == 4

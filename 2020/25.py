# https://adventofcode.com/2020/day/25
from collections import defaultdict
from timeit import default_timer as timer

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

def shared_encryption_key(card_public_key, door_public_key, use_cache=False, trace=True):
  cache = defaultdict(dict) # subject_num -> {loops -> value}
  def transform(subject_num, loops : int) -> int: 
    if use_cache and loops in cache[subject_num]: return cache[subject_num][loops] # no perf improvement? hmmm
    value = 1
    for _ in range(loops):
      value *= subject_num
      value %= 20201227
    if use_cache: cache[subject_num][loops] = value
    return value
  assert_equals(transform(subject_num=7, loops=8), 5764801)
  def compute_loop_size(subject_num : int, search_for : int, status_update_freq=10_000):
    timer()
    loops = 1
    while transform(subject_num, loops) != search_for: 
      loops +=1
      if trace and loops % status_update_freq == 0: print(f"handshake_status loops {loops} elapsed {timer()}")
    return loops

  # handshake
  timer()
  if trace: print(f"handshake_start card {card_public_key} door {door_public_key} use_cache {use_cache}")
  card_loops = compute_loop_size(subject_num=7, search_for=card_public_key)
  if trace: print(f"handshake_card {card_loops} elapsed {timer()}")
  # door_loops = compute_loop_size(subject_num=7, search_for=door_public_key)
  # if trace: print(f"handshake_door {door_loops} elapsed {timer()}")
  if trace: print(f"handshake_end")

  # encryption keys
  shared_encryption_key = transform(subject_num=door_public_key, loops=card_loops)
  # assert_equals(          transform(subject_num=card_public_key, loops=door_loops), shared_encryption_key)
  if trace: print(f"encryption_key {shared_encryption_key} elapsed {timer()}")
  return shared_encryption_key

# assert_equals(shared_encryption_key(card_public_key=5764801, door_public_key=17807724, trace=False), 14897079)

print(f"\npart 1: encryption key: {shared_encryption_key(15335876, 15086442, use_cache=True)}")
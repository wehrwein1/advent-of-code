from typing import List, Dict
from functools import reduce
from timeit import default_timer as timer

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def product(numbers : List[int]):     return reduce(lambda x, y: x * y, numbers)

def to_linked_list(cups):
  return dict( zip( map(int, [cups[-1], *cups[:-1]]), map(int, cups)))

def debug(linked_list : Dict[int, int], delim=' -> ') -> str:
  active_nodes = [key for key,value in linked_list.items() if not value is None]
  min_key = min(active_nodes)
  current = min_key
  links = []
  while True:
    links += [f"{current if current == min_key else ''}{delim}{linked_list[current]}"]
    if len(links) == len(active_nodes): break
    current = linked_list[current]
  return ''.join(links)
assert_equals(debug(to_linked_list('389125467')), "1 -> 2 -> 5 -> 4 -> 6 -> 7 -> 3 -> 8 -> 9 -> 1")
assert_equals(to_linked_list('389125467'), {7: 3, 3: 8, 8: 9, 9: 1, 1: 2, 2: 5, 5: 4, 4: 6, 6: 7})
assert_equals(to_linked_list([3,8,9,1,2,5,4,6,7]), {7: 3, 3: 8, 8: 9, 9: 1, 1: 2, 2: 5, 5: 4, 4: 6, 6: 7})

def take(num : int, linked_list : Dict[int,int], start_at):
  results = []
  current = start_at
  while len(results) < num:
    result = linked_list[current]
    results += [result]
    current = result
  linked_list[start_at] = linked_list[current] # disconnect first of 3
  linked_list[results[0]] = None
  linked_list[results[1]] = None
  linked_list[results[2]] = None
  return results
test_linked_list = to_linked_list('389125467')
assert_equals(debug(test_linked_list), "1 -> 2 -> 5 -> 4 -> 6 -> 7 -> 3 -> 8 -> 9 -> 1")
assert_equals(take(3, test_linked_list, start_at=3), [8,9,1])
assert_equals(debug(test_linked_list), "2 -> 5 -> 4 -> 6 -> 7 -> 3 -> 2")

def find_destination(linked_list : Dict[int,int], start_at : int, excluding : List[int]):
  current = start_at - 1
  active_nodes = set([key for key,value in linked_list.items() if not value is None]) # TODO FIXME performance
  # active_nodes = active_nodes - set(excluding) # for testing only
  min_active_node = None
  while current not in active_nodes:
    current -= 1
    if min_active_node is None: min_active_node = min(active_nodes) # small perf optimization
    if current < min_active_node: current = max(active_nodes) # TODO FIXME performance
  return current
assert_equals(find_destination(to_linked_list('389125467'), start_at=3, excluding=[8,9,1]), 2)
# assert_equals(find_destination(to_linked_list('389125467'), start_at=2, excluding=[8,9,1]), 7)

def simulate(cups : str, num_moves : int, result_delim=''):
  is_part1 = result_delim == ''
  move_count = 0
  if ',' in cups: cups = map(int, cups.split(','))
  current_cup : int = int(cups[0])
  linked_list : Dict[int,int] = to_linked_list(cups)
  # print(f"Initial state: {debug(linked_list)}")
  if not is_part1: print(f"Loaded / created linked list, elapsed(s): {timer()}")
  while move_count < num_moves:
    three_cups = take(3, linked_list, start_at=current_cup)
    dest_cup = find_destination(linked_list, start_at=current_cup, excluding=three_cups)
    # print(f"Move {move_count+1}, cups: ({current_cup}) {debug(linked_list, delim='')},    pick: {three_cups}, dest: {dest_cup}")
    next_current = linked_list[current_cup]
    linked_list[three_cups[2]] = linked_list[dest_cup]                    # link third of 3 -> dest cup's prior follower (disconnect dest cup)
    linked_list[three_cups[1]] = three_cups[2]                            # link second of 3 -> third of 3
    linked_list[three_cups[0]] = three_cups[1]                            # link first of 3 -> second of 3
    linked_list[dest_cup] = three_cups[0]                                 # link dest -> first of 3
    # assert all([not value is None for value in linked_list.values()])
    current_cup = next_current
    # print(f"         cups: ({current_cup}) {debug(linked_list, delim='')}")
    move_count +=1
    if not is_part1 and move_count % 100 == 0: print(f'Moves: {move_count}: elapsed(s): {timer()}') 
  result = debug(linked_list, delim=result_delim)
  if is_part1: result = result.replace('1','') # adjust results for printing
  return result
assert_equals(simulate(cups='389125467', num_moves=10),  '92658374')
assert_equals(simulate(cups='389125467', num_moves=100), '67384529')

# part 1
crab_cups = list(map(int, list('362981754')))
print(f"part 1: cups after 100 moves: {simulate(cups=crab_cups, num_moves=100)}")

# part 2
timer() # start time measurement
def numbers_after_one(numbers : List[int]):
  index = numbers.index(1)
  first =  numbers[index + 1]
  second = numbers[index + 2]
  print(f"numbers after one: {first}, {second}")
  return [first, second]
NUM_CUPS =  1_000_000
NUM_MOVES = 10_000_000
# NUM_CUPS =  100 #1_000_000
# NUM_MOVES = 10_000 #10_000_000

crab_cups = list(map(int, list('362981754')))
one_million_cups = crab_cups + list(range(max(crab_cups) + 1, NUM_CUPS + 1))
# crab_cups = list(map(int, list('389125467'))) # for testing only, part 2 description 
# one_million_cups = crab_cups # for test only 

assert_equals(one_million_cups[0:12], [3, 6, 2, 9, 8, 1, 7, 5, 4, 10, 11, 12])
assert_equals(one_million_cups[-1], NUM_CUPS)
sequence = simulate(cups=one_million_cups, num_moves=NUM_MOVES, result_delim=',')
# sequence = simulate(cups=one_million_cups, num_moves=10, result_delim=',')
print(f"part 2: product of two numbers after 1: {product(numbers_after_one(list(map(int, sequence.split(',')))))}")
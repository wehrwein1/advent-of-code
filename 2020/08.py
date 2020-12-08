# https://adventofcode.com/2020/day/8
from typing import Dict, List, Tuple

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

# functions

lines = [line for line in map(str.rstrip, open('input/08_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/08_TEST.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))

visited = set()
accumulator = 0
current_address : int = 0
next_address : int = 0
while not current_address in visited:
  instruction = lines[current_address]
  print("i={}, instruction='{}'".format(current_address, instruction))

  # execute
  op_code, argument = instruction.split(' ', 1) 
  if op_code == 'acc': 
    accumulator += int(argument)
    next_address = current_address + 1
  elif op_code == 'jmp':
    next_address += int(argument)
  elif op_code == 'nop':
    next_address = current_address + 1
  
  # next loop
  visited.add(current_address)
  current_address = next_address
  print(" visited={}, accum={}".format(list(visited), accumulator))

print('accumulator before entering infinite loop:', accumulator)
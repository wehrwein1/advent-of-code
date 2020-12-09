# https://adventofcode.com/2020/day/8
from typing import Dict, List, Tuple, Callable
from enum import Enum, auto

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

# instruction set
instruction_set : Dict[str, Callable[[int,int,str],List[int]]] = dict( { # returns accumulator, next_address
  'acc' : lambda accumulator, current_address, op_arg : (accumulator + int(op_arg), current_address + 1),
  'jmp' : lambda accumulator, current_address, op_arg : (accumulator              , current_address + int(op_arg)),
  'nop' : lambda accumulator, current_address, _      : (accumulator              , current_address + 1)
})
assert_equals(instruction_set['acc'](5,0,'77'), (82,1)) # acc: accumulator += op_arg, address +=1
assert_equals(instruction_set['acc'](3,1,'5'),  (8,2))  # acc: accumulator += op_arg, address +=1
assert_equals(instruction_set['jmp'](5,0,'77'), (5,77)) # jmp: address += op_arg
assert_equals(instruction_set['jmp'](3,1,'5'),  (3,6))  # jmp: address += op_arg
assert_equals(instruction_set['nop'](5,0,'77'), (5,1))  # nop: address +=1
assert_equals(instruction_set['nop'](3,1,'5'),  (3,2))  # nop: address +=1

# functions
def execute_program(instructions : List[str]) -> Tuple[int, bool, bool]:
  visited = set()
  accumulator = 0
  current_address : int = 0
  next_address : int = 0
  # print('Run program: {}'.format(instructions))
  def is_infinite_loop(): return current_address in visited
  def is_terminated_normally(): return current_address >= len(instructions) 
  while not is_infinite_loop() and not is_terminated_normally():
    instruction = instructions[current_address]
    # print("i={}, instruction='{}'".format(current_address, instruction))
    # execute current instruction
    op_code, op_arg = instruction.split(' ', 1)
    accumulator, next_address = instruction_set[op_code](accumulator, current_address, op_arg)
    # if op_code == 'acc': 
    #   accumulator += int(op_arg)
    #   next_address = current_address + 1
    # elif op_code == 'jmp':
    #   next_address += int(op_arg)
    # elif op_code == 'nop':
    #   next_address = current_address + 1
    # next loop
    visited.add(current_address)
    current_address = next_address
    # print(" visited={}, accum={}".format(list(visited), accumulator))
  return accumulator, is_infinite_loop(), is_terminated_normally()
assert_equals(execute_program(instructions=[line for line in map(str.rstrip, open('input/08_TEST.txt'))]),  (5, True, False))
assert_equals(execute_program(instructions=[line for line in map(str.rstrip, open('input/08_TEST2.txt'))]), (8, False, True))

lines = [line for line in map(str.rstrip, open('input/08_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/08_TEST.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))
print('\npart 1 result:', execute_program(lines))

# find buggy instruction
for address, instruction in enumerate(lines):
  modified_program = []
  modified_instruction = None
  print("checking address", address, instruction)
  if instruction.startswith('nop'): 
    modified_instruction = instruction.replace('nop','jmp') 
    modified_program = [line for line in map(str.rstrip, open('input/08_INPUT.txt'))]
    modified_program[address] = modified_instruction
  elif instruction.startswith('jmp'): 
    modified_instruction = instruction.replace('jmp','nop')
    modified_program = [line for line in map(str.rstrip, open('input/08_INPUT.txt'))]
    modified_program[address] = modified_instruction
  if modified_program:
    accumulator, is_infinite_loop, is_terminated_normally = execute_program(instructions=modified_program)
    if is_terminated_normally: 
      print("\npart 2 changed instruction #{} from '{}' ->'{}'".format(address, instruction, modified_instruction))
      print("part 2 accumulator:", accumulator)
      exit(0)

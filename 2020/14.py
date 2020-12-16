# https://adventofcode.com/2020/day/14
from typing import List, Dict

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]

def set_char(text : str, i : int, one_char : str): # Note: O(n), eek
  buffer = list(''.join(text))
  buffer[i:i+1] = one_char
  return ''.join(buffer)

def set_bit_one(buffer : int, bit_index : int) -> int: buffer |= 1 << bit_index; return buffer
assert_equals(set_bit_one(0, 0), 1)
assert_equals(set_bit_one(16,3), 24) # b10000 with b01000 -> b11000

def set_bit_zero(buffer : int, bit_index : int, bitmask_len : int) -> int: 
  mask = (1 << bitmask_len + 1) - 1 
  mask -= 1 << bit_index
  buffer &= mask
  return buffer
assert_equals(set_bit_zero(31, 0, bitmask_len=5), 30) # b11111 with b11110
assert_equals(set_bit_zero(28, 3, bitmask_len=5), 20) # b11100 with b10111

def allocate_memory(lines : List[str], is_part1=True) -> Dict[int, int]:
  memory : Dict[int, int] = dict()
  active_bitmask : Dict[int, int] = dict()
  bitmask = None
  bitmask_len = None
  addresses = [] # part 2
  for line_index, line in enumerate(lines):
    if line.startswith('mask = '):
      print('line {}: {}'.format(line_index, line))
      bitmask = line.split(' = ')[1]
      bitmask_len = len(bitmask)
      active_bitmask : Dict[int, int] = dict()
      assert_equals(len(bitmask), 36)
      for i, char in enumerate(reversed(bitmask)):
        if char != 'X': active_bitmask[i] = int(char)  # 2^i = value, zero-indexed
      print(' new bitmask:', active_bitmask)
      addresses : List[int] = list()
      continue
    assignment, value = map(str.strip, line.split(' = '))
    address = assignment.split('[')[1].split(']')[0]

    # process assignment    
    if is_part1:
      bit_value = int(value)
      print('line: {}, assigning value {}'.format(line, bin(bit_value)))
    else: 
      bit_value = int(address)
      print('line {}: {}, assigning at fuzzy address ~{}, ~{}'.format(line_index, line, address, bin(int(address))))
    # apply bitmask    
    for mask_index, mask_value in active_bitmask.items():
      if is_part1: # part 1: compute bit value
        if mask_value == 1: 
          res = mask_value << mask_index # 1 followed by (mask_index) zeros
          bit_value |= res # set bit: OR with 1
          operation_name = "OR"
        elif mask_value == 0:
          res = (1 << bitmask_len + 1) - 1
          res -= 1 << mask_index
          bit_value &= res
          operation_name = "AND"
        else: raise SystemError(mask_value)
        print(' bitmask 2^{} = {}: {} {}, result: {} = {}'.format(mask_index, mask_value, operation_name, bin(res), bit_value, bin(bit_value)))
      else: # part 2: compute addresses
        if mask_value == 1: 
          res = mask_value << mask_index # 1 followed by (mask_index) zeros
          bit_value |= res # set bit: OR with 1
        # process result with x's, collect 2^(#x) addresses per assignment    
    # set memory
    # def add_exes(text : str, x_indices : List[int]) -> str:
    #   result = text
    #   for x_index in x_indices:
    #     result = set_char(result, bitmask_len - x_index + len(text) - 2, 'x')
    #   return result
    # assert_equals(add_exes('0101', [35]), '010x')
    # assert_equals(add_exes('0101', [34,35]), '010xx')
    # assert_equals(add_exes('11010', [32,34,35]), '1101xx')
    if is_part1:
      print(' mem[{}] = {}'.format(address, bit_value))
      memory[address] = bit_value
    else:
      # scan bitmask, find 'X' bits, compute addresses
      fuzzy_indices = [ i for i in range(bitmask_len) if bitmask[i] == 'X']
      print(' fuzzy address after 1s apply {}: {}, len={} {}'.format(list(reversed([ key for key, value in active_bitmask.items() if value == 1])), bin(bit_value), len(fuzzy_indices), fuzzy_indices))
      for permutation in range(0, 1 << len(fuzzy_indices)):
        buffer = int(bit_value)
        permutation_str = str(bin(permutation)).split('b')[1]
        if len(permutation_str) < len(fuzzy_indices):
          permutation_str = ('0' * (len(fuzzy_indices) - len(permutation_str))) + permutation_str
        for i, bit in enumerate(permutation_str):
          # print('   i={} {}'.format(i, bit))
          if int(bit) == 1: buffer = set_bit_one(buffer, bitmask_len - fuzzy_indices[i] - 1)
          if int(bit) == 0: buffer = set_bit_zero(buffer, bitmask_len - fuzzy_indices[i] - 1, bitmask_len=bitmask_len)
        # print('  -> permutation: {} -> apply to buffer {} -> computed address {} {}'.format(permutation_str, bin(bit_value)[2:], bin(buffer), buffer))
        addresses.append(buffer)

      # print(' mem[{}] = {}'.format(addresses, int(value)))
      for addr in addresses:
        memory[addr] = int(value)
  # print('finished, memory:', memory)
  return memory
assert_equals(sum(allocate_memory(load_file('input/14_TEST.txt')).values()), 165)
assert_equals(allocate_memory(load_file('input/14_TEST2.txt'), is_part1=False), {26: 1, 27: 1, 58: 100, 59: 100, 16: 1, 17: 1, 18: 1, 19: 1, 24: 1, 25: 1} )
assert_equals(sum(allocate_memory(load_file('input/14_TEST2.txt'), is_part1=False).values()), 208)

print('part 1 sum memory values:', sum(allocate_memory(load_file('input/14_INPUT.txt')).values()))
print('part 2 sum memory values:', sum(allocate_memory(load_file('input/14_INPUT.txt'), is_part1=False).values()))

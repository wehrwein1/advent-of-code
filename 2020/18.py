# Disclaimer: Maintainability/understandability is the primary software cost driver of software generally 
# (https://ieeexplore.ieee.org/abstract/document/6650541), but Advent of code is a speed-based coding challenge
# not subject to those constraints. Would be an exercise to simplify, reduce duplication, and optimize performance.

# https://adventofcode.com/2020/day/18
from typing import Callable
from pyutil.fileio import file_lines
from pyutil.testing import assert_equals

def parened(text):                    return '({})'.format(text if text is str else ' '.join(text))
def remove_all(text, remove_chars):
  for remove_char in remove_chars:
    text = text.replace(remove_char, '')
  return text
assert_equals(remove_all('(abcd)',   ['(',')']), 'abcd')
assert_equals(remove_all('(ab)(cd)', ['(',')']), 'abcd')

def find_boundary(expr : str, is_valid_expression : Callable, start_pos=0, OPEN='(', CLOSE=')'):
  assert OPEN in expr, f"Found no open '{OPEN}' in '{expr}'"
  balance = 0
  header_tokens = []
  header_start_pos = start_pos
  close_pos = None
  while not (is_valid_expression(header_tokens) and balance == 0):
    open_pos  = expr.index(OPEN,  start_pos) if OPEN  in expr[start_pos:] else None
    close_pos = expr.index(CLOSE, start_pos) if CLOSE in expr[start_pos:] else None
    boundary = min(filter(lambda pos : not pos is None, [open_pos, close_pos]))
    balance = balance + 1 if boundary == open_pos else balance - 1 # None safe comparison
    if balance == 0:
      header_tokens += list(expr[header_start_pos:boundary+1])
      header_start_pos = boundary + 1
    start_pos = boundary + 1
  tail = expr[start_pos:].strip()
  return ''.join(header_tokens), tail

def count_numbers(text_or_char_array):
  if type(text_or_char_array) == str: return count_numbers(text_or_char_array.split(' '))
  return len(list(filter(lambda char : char.isnumeric(), text_or_char_array)))
assert_equals(count_numbers('abc'), 0)
assert_equals(count_numbers('a 1 c'), 1)
assert_equals(count_numbers('6 and 7'), 2)
assert_equals(count_numbers(['6','+','7']), 2)
assert_equals(count_numbers('63 + 7'), 2)

def tokenize_expression(expr : str):
  if not any(map(lambda paren : paren in expr, ['(',')'])):
    tokens = expr.split(' ')
    head, tail = tokens[0:3], tokens[3:]
    return ' '.join(head), ' '.join(tail)
  is_valid_numeric_expression = lambda header_tokens : count_numbers(header_tokens) >= 2
  return find_boundary(expr, is_valid_expression=is_valid_numeric_expression, start_pos=0)
assert_equals(tokenize_expression('1'), ('1', ''))
assert_equals(tokenize_expression('1 + 2'), ('1 + 2', ''))
assert_equals(tokenize_expression('1 + 2 + 3'), ('1 + 2', '+ 3'))
assert_equals(tokenize_expression('1 + 2 + 3 * 4'), ('1 + 2', '+ 3 * 4'))
assert_equals(tokenize_expression('(1 + 2)'), ('(1 + 2)', ''))
assert_equals(tokenize_expression('(1 + 2) + 3'), ('(1 + 2)', '+ 3'))
assert_equals(tokenize_expression('1 + (2 * 3) + 4'), ('1 + (2 * 3)', '+ 4'))
assert_equals(tokenize_expression('(((1 + 2))) + 3'), ('(((1 + 2)))', '+ 3'))

def evaluate_expr(expr : str, is_part1=True) -> int:
  if not ' ' in expr: return int(expr)
  head, tail = tokenize_expression(expr)
  print(f" head: '{head}'")
  print(f" tail: '{tail}'")
  # evaluate
  try:
    if count_numbers(remove_all(head, ['(',')'])) == 2:
      head_val = eval(head)
    else:
      if head.startswith('(') and head.endswith(')'):
        head = head[1:-1]
      elif head.endswith(')'):
        sub_expr_pos = head.index('(')
        sub_expr = head[sub_expr_pos:]
        sub_expr_val = evaluate_expr(sub_expr)
        head = head[0:sub_expr_pos] + str(sub_expr_val)
      elif head.startswith('('):
        raise SystemError('not implemented')
      head_val = evaluate_expr(head)
    print(f" head: ({head}) -> {head_val}")
    print(f" tail: {tail}")
    if not tail: return head_val
    expr = f'{head_val} {tail}'
    return evaluate_expr(expr)
  except SyntaxError as e:
    raise Exception(f"Error evaluating expr '{expr}': {e}")  
# part 1
assert_equals(evaluate_expr('1'), 1)
assert_equals(evaluate_expr('1 + 6'), 7)
assert_equals(evaluate_expr('1 + 2 * 3'), 9)
assert_equals(evaluate_expr('1 + 2 * 3 + 4 * 5 + 6'), 71)
assert_equals(evaluate_expr('(2 + 3)'), 5)
assert_equals(evaluate_expr('(2 * 3)'), 6)
assert_equals(evaluate_expr('(2 * 3) + 1'), 7)
assert_equals(evaluate_expr('(2 + 3 * 4)'), 20)
assert_equals(evaluate_expr('1 + (2 * 3) + (4 * (5 + 6))'), 51)
assert_equals(evaluate_expr('2 * 3 + (4 * 5)'), 26)
assert_equals(evaluate_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
assert_equals(evaluate_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)
assert_equals(evaluate_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)

# part 2
assert_equals(evaluate_expr('1 + (2 * 3) + (4 * (5 + 6))', is_part1=False), 51)
assert_equals(evaluate_expr('1 + 2 * 3 + 4 * 5 + 6', is_part1=False), 231)

print(f"part 1: sum of all expr values: {sum(map(evaluate_expr, file_lines('2020/input/18_INPUT.txt')))}")
print(f"part 2: sum of all expr values: {sum(map(lambda line: evaluate_expr(line, is_part1=False), file_lines('2020/input/18_INPUT.txt')))}")
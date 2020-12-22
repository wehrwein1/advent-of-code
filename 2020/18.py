# Disclaimer: given that AoC is a speed-based challenge, this code is optimized for development and debugging speed 
# not maintainability. In general, maintainability/understandability is the primary cost driver of software overall 
# -- I've written about this previously: https://ieeexplore.ieee.org/abstract/document/6650541. This is not 
# necessarility reflective of what I consider "good" production-quality code. Would be an exercise to simplify, 
# reduce duplication, optimize big O runtime performance, and make it more self-documenting.

# https://adventofcode.com/2020/day/18
from typing import List, Dict, Tuple
from collections import defaultdict
from functools import reduce

def assert_equals(actual, expected):  assert actual == expected, "\n expected: '{}'\n actual:   '{}'".format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def parened(text):                    return '({})'.format(text if text is str else ' '.join(text))

# def rewrite_expr(expr : str) -> str:
#   print("expr: '{}'".format(expr))
#   # if not expr: return expr
#   # if not expr.startswith('(') and not expr.endswith(')'):
#   #   return rewrite_expr('(' + expr + ')')
#   if not ' ' in expr: return expr
#   tokens = expr.split(' ')
#   print(f'tokens: {tokens}')
#   if len(tokens) == 3: return parened(tokens[0:3])
#   if len(tokens) == 5: return "({}) {}".format(parened(tokens[0:3]), ' '.join(tokens[3:]))
  
#   head, tail = expr[0:4], expr[5:]
#   print(" head: '{}'".format(head))
#   print(" tail: '{}'".format(tail))
#   if not head: return expr
#   # if not tail: return parened(head)
#   if not tail: return head
#   return '({} {})'.format(head, rewrite_expr(tail))
# assert_equals(rewrite_expr(''), '')
# assert_equals(rewrite_expr('5'), '5')
# assert_equals(rewrite_expr('1 + 2'), '(1 + 2)')
# assert_equals(rewrite_expr('1 + 2 + 3'), '((1 + 2) + 3)')
# assert_equals(rewrite_expr('1 + 2 * 3 + 4 * 5 + 6'), '(((((1 + 2) * 3) + 4) * 5) + 6)')

# def evaluate_expr(expr : str) -> int:
#   try:
#     return eval(rewrite_expr(expr))
#   except SyntaxError as e:
#     raise SyntaxError("Error evaluating expr '{}': {}".format(expr, e))

def evaluate_expr(expr : str) -> int:
  if not ' ' in expr: return int(expr)
  tokens = expr.split(' ')
  head, tail = tokens[0:3], tokens[3:]
  print(f"expr:   {' '.join(tokens)}")
  # assume no parens
  try:  
    head_val = eval(' '.join(head))
    print(f" head: ({' '.join(head)}) -> {head_val}")
    print(f" tail: {tail}")
    if not tail: return head_val
    print(f"tail0={tail[0]}")
    print(f"tail*={tail[1:]}")
    new_expr = f'{head_val} {tail[0]} {" ".join(tail[1:])}'
    # print(f"new expr:", new_expr)
    return evaluate_expr(new_expr)
  except Exception as e:
    raise Exception("Error evaluating expr '{}': {}".format(expr, e))
  
# part 1
assert_equals(evaluate_expr('1'), 1)
assert_equals(evaluate_expr('1 + 6'), 7)
assert_equals(evaluate_expr('1 + 2 * 3 + 4 * 5 + 6'), 71)
# part 1 parens
assert_equals(evaluate_expr('(2 + 3)'), 5)
assert_equals(evaluate_expr('(2 * 3)'), 6)
assert_equals(evaluate_expr('(2 * 3) + 1'), 7)
assert_equals(evaluate_expr('(2 * 3 + 1)'), 7)

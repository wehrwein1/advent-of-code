# https://adventofcode.com/2020/day/6
import string
from typing import List

lines = [line for line in map(str.rstrip, open('input/06_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/06_TEST.txt'))]
print('input (len={}): {}'.format(len(lines), lines))

def separate_by_empty_lines(lines : List[str]) -> List[List[str]]:
  i : int = 0
  groups = []
  while i < len(lines):  
    line = lines[i]
    current_group = []
    while not len(line) == 0:
      current_group.append(line)
      i += 1
      line = lines[i] if i < len(lines) else '' # advance inner loop
    groups.append(current_group)
    i += 1
  return groups

def encode_customs_form(line : str):
  person_questions = set(list(line))
  return [1 if char in person_questions else 0 for char in string.ascii_lowercase] # a-z is 26 bits, luckily python int is 32 (ok)
assert encode_customs_form('a')   == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert encode_customs_form('abc') == [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert encode_customs_form('d')   == [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert encode_customs_form('z')   == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

def count_group_yeses(customs_forms: List[str]) -> int:
  group_questions = set()
  for customs_form in customs_forms:
    group_questions |= set(list(customs_form))
  return len(group_questions)
assert count_group_yeses(['abc'])           == 3
assert count_group_yeses(['a','b','c'])     == 3
assert count_group_yeses(['ab','ac'])       == 3
assert count_group_yeses(['a','a','a','a']) == 1
assert count_group_yeses(['b'])             == 1

def count_group_same_question_yeses(customs_forms : List[str]) -> int:
  encodings = map(encode_customs_form, customs_forms)
  group_encoding : int = 2**len(string.ascii_lowercase)-1 # all ones
  for person_encoding in encodings:
    person_binary : str = ''.join([str(s) for s in person_encoding])
    group_encoding = group_encoding & int(person_binary, 2)
    print(' person_binary: {}, group={}'.format(person_binary, bin(group_encoding)))
  count = len([ones for ones in bin(group_encoding) if ones == '1'])
  print('  count={}'.format(count))
  return count
assert count_group_same_question_yeses(['abc'])           == 3
assert count_group_same_question_yeses(['a','b','c'])     == 0
assert count_group_same_question_yeses(['ab','ac'])       == 1
assert count_group_same_question_yeses(['a','a','a','a']) == 1
assert count_group_same_question_yeses(['b'])             == 1

groups = separate_by_empty_lines(lines)
question_counts = [count_group_same_question_yeses(group) for group in groups]
# print("sum 'yes' counts:", sum(count_group_yeses(group) for group in groups))
print("sum 'all same question' yes counts:", sum(question_counts))
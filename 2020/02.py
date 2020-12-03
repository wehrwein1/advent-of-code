from typing import List

# https://adventofcode.com/2020/day/2
lines = [line for line in map(str.rstrip, open('input/02_INPUT.txt'))]
# lines = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
print('input (len={}): {}'.format(len(lines), lines))

def is_valid_password_part1(password : str, policy_range : List[int], policy_char : str):
  char_count = sum([1 for ch in password if ch == policy_char])
  min_allowed, max_allowed = policy_range
  return char_count >= min_allowed and char_count <= max_allowed
  min_allowed, max_allowed = map(int, char_range.split('-'))

def is_valid_password_part2(password : str, policy_range : List[int], policy_char : str):
  first, second = policy_range
  return (password[first-1] == policy_char) ^ (password[second-1] == policy_char)

valid_count : int = 0
for line in lines:
  policy, password = map(str.strip, line.split(':'))
  policy_range, policy_char = policy.split(' ')
  # is_valid = is_valid_password_part1(password, map(int, policy_range.split('-')), policy_char)
  is_valid = is_valid_password_part2(password, map(int, policy_range.split('-')), policy_char)
  print('line: \'{}\' -> {}'.format(line, is_valid))
  if is_valid:
    valid_count += 1
print("valid:", valid_count)
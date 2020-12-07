# https://adventofcode.com/2020/day/7
import string
from typing import List
import numpy as np
from scipy import sparse

def assert_equals(actual, expected): 
  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)

# functions
def parse_rule(luggage_rule: str):
  def remove_bags(text : str) -> str: return text.split('bag')[0].strip()
  def parse_dependency(text : str): 
    if 'no other' in text: return dict()
    items = [tuple(reversed(item.split(' ',1))) for item in list(map(remove_bags, targets_token.split(',')))]
    return dict(items)
  source_token, targets_token = map(str.strip, luggage_rule.split(' contain '))
  targets = map(str.strip, targets_token.split(','))
  return remove_bags(source_token), parse_dependency(targets_token)
assert_equals(parse_rule('light red bags contain 1 bright white bag, 2 muted yellow bags.'), ('light red', dict({'bright white' : '1', 'muted yellow': '2'})))
assert_equals(parse_rule('faded blue bags contain no other bags.'), ('faded blue', dict()))

def find_unique_bag_colors(rules : dict) -> List[str]:
  bags_set = set()
  for (source, targets) in rules.items():
    bags_set.add(source)
    for bag in targets: bags_set.add(bag)
  return sorted(list(bags_set))
  
def compute_reachability_matrix(bags : List[str], rules : dict):
  dim = len(bags)
  matrix = np.array([[0 for i in range(dim)] for j in range(dim)])
  # print('matrix:\n', matrix)
  # populate matrix
  for source, target_pairs in rules.items():
    source_index = bags.index(source)
    for target_bag in target_pairs:
      target_index = bags.index(target_bag)
      weight = int(target_pairs[target_bag])
      matrix[source_index][target_index] = weight
  # print('matrix:\n', matrix)
  # for i, bag in enumerate(bags):
  #   print(" {}: {}".format(i, bag))
  np.fill_diagonal(matrix, 1)
  return np.linalg.matrix_power(matrix, dim)

def count_colors_reachable(bags : List[str], rules : dict) -> int:
  reachability_matrix = compute_reachability_matrix(bags, rules)
  # print('reachability:\n', reachability_matrix)
  i = bags.index('shiny gold')
  print('shiny gold index=', i)
  row = reachability_matrix[i,:]
  col = reachability_matrix[:,i]
  # print('row {}: {}, count={}'.format(i, row if len(row) < 10 else 'row', sum([1 for item in row if item > 0])))
  # print('col {}: {}, count={}'.format(i, col if len(col) < 10 else 'col', sum([1 for item in col if item > 0])))
  colors_count = 0
  for i, item in enumerate(list(str(col).replace('[','').replace(']','').split())):
    if i == bags.index('shiny gold'): continue
    if not item == '0':
      # print('\"{}\" can contain shiny gold bags (index {})'.format(bags[i], i))
      colors_count += 1  
  return colors_count

lines = [line for line in map(str.rstrip, open('input/07_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/07_TEST.txt'))]
# lines = [line for line in map(str.rstrip, open('input/07_TEST2.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))

# parse rules
rules = dict( parse_rule(rule) for rule in lines)
print('Found rules ({}):'.format(len(rules)))
for rule in rules: print(" rule: '{}', {}".format(rule, rules[rule]))

# part 1
bags = find_unique_bag_colors(rules)
# print('Found bag colors ({})'.format(len(bags), bags))
print('part 1 colors count:', count_colors_reachable(bags, rules))

# part 2
def count_bags_inside(num : int, bag_color : str) -> int: # count is inclusive of itself
  contained_bag_counts : dict = rules[bag_color] # bag -> count
  if not contained_bag_counts: return num
  return num + sum([num * count_bags_inside(int(contained_bag_counts[bag]), bag) for bag in contained_bag_counts])
# assert_equals(count_bags_inside(1, 'dotted black'), 1)
# assert_equals(count_bags_inside(1, 'faded blue'), 1)
# assert_equals(count_bags_inside(1, 'vibrant plum'), 1 + (5+6))
# assert_equals(count_bags_inside(2, 'vibrant plum'), 2 + 2* (5+6))
print('part 2 bags count:', count_bags_inside(1, 'shiny gold') - 1) # -1 to exclude the gold bag
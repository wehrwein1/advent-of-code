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

lines = [line for line in map(str.rstrip, open('input/07_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/07_TEST.txt'))]
print('\ninput (len={}): {}'.format(len(lines), lines))

# parse rules
rules = [parse_rule(rule) for rule in lines]
print('Found rules ({})'.format(len(rules)))
for rule in rules: print("rule={}".format(rule))

# build empty matrix
bags_set = set()
for (source, targets) in rules:
  bags_set.add(source)
  for bag in targets: bags_set.add(bag)
bags = sorted(list(bags_set))
print('Found colors ({}): {}'.format(len(bags), bags))
dim = len(bags)
matrix = np.array([[0 for i in range(dim)] for j in range(dim)])
# print('matrix:\n', matrix)

# populate matrix
# np.fill_diagonal(matrix, 1)
for source, target_pairs in rules:
  source_index = bags.index(source)
  # print('target_pairs', target_pairs)
  for target_bag in target_pairs:
    target_index = bags.index(target_bag)
    weight = int(target_pairs[target_bag])
    matrix[source_index][target_index] = weight
print('matrix:\n', matrix)

# count
# import networkx as nx
# G = nx.DiGraph(matrix)       # directed because A need not be symmetric
# paths = nx.all_pairs_shortest_path_length(G)
# indices = []
# indptr = [0]
# for row in paths:
#   reachable = [v for v in row[1] if row[1][v] > 0]
#   indices.extend(reachable)
#   indptr.append(len(indices))
# data = np.ones((len(indices),), dtype=np.uint8)
# A_trans = matrix + sparse.csr_matrix((data, indices, indptr), shape=matrix.shape)
# print(matrix, "\n\n", A_trans)



# G=nx.DiGraph(matrix)
# A=nx.minimum_spanning_arborescence(G)
# for node in A.nodes():
#   s = list(nx.descendants(A, node))
#   matrix[s, node] = 1

# print("reachability:\n", matrix)
# exit()

np.fill_diagonal(matrix, 1)
print('diag set:\n', matrix)
# print("matrix power:\n", matrix ** dim)

for i, bag in enumerate(bags):
  print(" {}: {}".format(i, bag))
i = bags.index('shiny gold')
print('index=', i)

reachability_matrix = np.linalg.matrix_power(matrix, dim)
print('reachability:\n', reachability_matrix)
row = reachability_matrix[i,:]
col = reachability_matrix[:,i]
print('row {}: {}, count={}'.format(i, row if len(row) < 10 else 'row', sum([1 for item in row if item > 0])))
print('col {}: {}, count={}'.format(i, col if len(col) < 10 else 'col', sum([1 for item in col if item > 0])))
# decode row for sanity check
print()
count = 0
for i, item in enumerate(list(str(col).replace('[','').replace(']','').split())):
  if i == bags.index('shiny gold'): print('skip diag'); continue
  if not item == '0':
    print('\"{}\" can contain shiny gold bags (index {})'.format(bags[i], i))
    count += 1
  
print("count:", count)
# print("matrix:\n", matrix)
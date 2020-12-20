# https://adventofcode.com/2020/day/20
from typing import List, Dict, Tuple
from functools import reduce
import re

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
def load_tiles(filename):             return list(map(Tile.create_from_data, partition(load_file(filename))))
def product(numbers : List[int]):     return reduce(lambda x, y: x * y, numbers)
def partition(lines : List[str], sep='', ignore='//'):
  active_lines = list(filter(lambda line : not line.startswith(ignore), lines))
  partitions = []
  for line in active_lines:
    if line == sep or not partitions:
      partitions.append([])
      if line != sep: partitions[-1].append(line)
      continue
    partitions[-1].append(line)
  return partitions

class Tile:
  @staticmethod
  def create_from_data(data : List[str]):
    num = match.group(1) if (match := re.search('Tile (\d{4}):', data[0], re.IGNORECASE)) else None
    return Tile(num, data[1:])
  def __init__(self, number, data : List[str]):
    self.number = number
    self.data = data
  def __str__(self) -> str:
      return "{}: {}".format(self.number, self.data)

def solve(tiles) -> List[List[int]]:
  for tile in tiles:
    print(tile)
  return [[0,0],[0,0]] # TODO FIXME
assert_equals(solve(load_tiles('input/20_TEST_sm.txt')), [[1,2], [3,4]])

def corners(tile_arrangement : List[List[int]]) -> List[int]:
  return [tile_arrangement[0][0],  tile_arrangement[0][-1],
          tile_arrangement[-1][0], tile_arrangement[-1][-1]]
assert_equals(corners([[1,2,3],[4,5,6],[7,8,9]]), [1,3,7,9])
assert_equals(product(corners([[1,2,3],[4,5,6],[7,8,9]])), 1*3*7*9)

print('part 1: product of corners:', product(corners(solve(load_tiles('input/20_INPUT.txt')))))

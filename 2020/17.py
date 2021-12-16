# Disclaimer: Maintainability/understandability is the primary software cost driver of software generally 
# (https://ieeexplore.ieee.org/abstract/document/6650541), but Advent of code is a speed-based coding challenge
# not subject to those constraints. Would be an exercise to simplify, reduce duplication, and optimize performance.

# https://adventofcode.com/2020/day/17
from typing import List, Dict, Tuple
from collections import Counter
import numpy
from pyutil.fileio import file_lines
from pyutil.testing import assert_equals

# part 1: apply change rules in three dimensions.
# Mark cells as either active (#) or inactive (.) 
# Count the number of active cubes after n cycles.

# How to model the cube space? 
# How to evaluate how many nearby active cubes in 3D?
# Use day 11 as a guide

def simulate(initial_z_zero_plane : List[str], num_cycles : int):
  dim = len(initial_z_zero_plane[0])
  data = numpy.zeros((dim, dim, dim), dtype=int)
  print(data)
  return initial_z_zero_plane

def counts(list_of_lists_of_strings) -> Dict[str, int]:
  return Counter(''.join(map(''.join, list_of_lists_of_strings)))

assert_equals(simulate(['.#.','..#', '###'], num_cycles=1), [['#..', '..#', '.#.'],  # z = -1
                                                             ['#.#', '.##', '.#.'],  # z = 0
                                                             ['#..', '..#', '.#.']]) # z = 1
assert_equals(simulate(['.#.','..#', '###'], num_cycles=2), [['.....', '.....', '..#..', '.....', '.....'],  # Z -2
                                                             ['..#..', '.#..#', '....#', '.#...', '.....'],  # z -1
                                                             ['##...', '##...', '#....', '....#', '.###.'],  # z  0
                                                             ['..#..', '.#..#', '....#', '.#...', '.....'],  # z  1
                                                             ['.....', '.....', '..#..', '.....', '.....']]) # z  2 
assert_equals(simulate(['.#.','..#', '###'], num_cycles=3), 
                [ ['.......', '.......', '..##...', '..###..', '.......', '.......', '.......'],  # Z -2
                  ['..#....', '...#...', '#......', '.....##', '.#...#.', '..#.#..', '...#...'],  # z -1 
                  ['...#...', '.......', '#......', '.......', '.....##', '.##.#..', '...#...'],  # z  0
                  ['..#....', '...#...', '#......', '.....##', '.#...#.', '..#.#..', '...#...'],  # z  1
                  ['.......', '.......', '..##...', '..###..', '.......', '.......', '.......']]) # z  2 
assert_equals(counts(simulate(['.#.','..#', '###'], num_cycles=6))['#'], 112)

print(f"part 1: count of active cubes: {counts(simulate(file_lines('2020/input/17_INPUT.txt')))}")

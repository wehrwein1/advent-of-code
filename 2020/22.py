# https://adventofcode.com/2020/day/22
from typing import List, Dict, Set, Tuple
from collections import defaultdict

def assert_equals(actual, expected):  assert actual == expected, '\n expected: {}\n actual:   {}'.format(expected, actual)
def load_file(filename):              return [line for line in map(str.rstrip, open(filename))]
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

def load_decks(filename):
  return list(map(lambda lst : list(map(int, lst[1:])), partition(load_file(filename))))
def score(deck : List[int]):
  score = 0
  for i, val in enumerate(reversed(deck)):
    score += (i+1) * val
  return score

def play_war(player_decks : list):
  player1 = player_decks[0]
  player2 = player_decks[1]
  i = 0
  while len(player1) != 0 and len(player2) != 0:
    p1card = player1[0]
    p2card = player2[0]
    # print(f'round {i+1}: {p1card} {p2card}')
    if p1card > p2card:
      player1 += [p1card, p2card]
    else:
      player2 += [p2card, p1card]
    player1 = player1[1:]
    player2 = player2[1:]
  winnning_hand = player1 if player1 else player2
  print(f'Player {1 if player1 else 2} won: {winnning_hand}')
  return winnning_hand
assert_equals(play_war(load_decks('input/22_TEST.txt')), [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
assert_equals(score(play_war(load_decks('input/22_TEST.txt'))), 306)

print(f'part 1: winning player score: {score(play_war(load_decks("input/22_INPUT.txt")))}')
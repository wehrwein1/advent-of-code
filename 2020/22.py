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

def play_war(initial_player_decks : list, state=defaultdict(list), state_depth=0, is_part1=True):
  # begin round
  player1_deck = initial_player_decks[0]
  player2_deck = initial_player_decks[1]
  i = 0
  while len(player1_deck) != 0 and len(player2_deck) != 0:
    # capture state, check for prior states
    if not is_part1:
      player_decks = (player1_deck, player2_deck)
      if player_decks in state[state_depth]: 
        print(f'Game {state_depth + 1} round {i+1}: player1 wins because this exact state seen before:', player_decks)
        del state[state_depth]
        return player_decks[0]
      state[state_depth].append(player_decks)
    # run the round
    player1_card = player1_deck[0]
    player2_card = player2_deck[0]
    is_player1_win = player1_card > player2_card
    round_winning_player = 1 if is_player1_win else 2
    if not is_part1:
      is_new_subgame = (len(player1_deck[1:]) >= player1_card) and \
                       (len(player2_deck[1:]) >= player2_card)
      if is_new_subgame:
        print(f'Game {state_depth + 1} round {i+1}: entering sub-game')
        print(f' Current decks: 1: {player1_deck}, drawn={player1_card}')
        print(f'                2: {player2_deck}, drawn={player2_card}')
        print(f' Subgame decks: 1: {player1_deck[1:]}')
        print(f'                2: {player2_deck[1:]}')
        subgame_winning_player, _ = play_war([player1_deck[1:], player2_deck[1:]], state=state, state_depth=state_depth+1, is_part1=is_part1)
        is_player1_win = subgame_winning_player == 'Player1'
        round_winning_player = 1 if is_player1_win else 2
        print(f'Game {state_depth+1} resuming, force player{round_winning_player} win..')
        # Do i need to bring the deck states back up?
    print(f'Game {state_depth+1} round {i+1}: {player1_card} vs {player2_card} -> win: player{round_winning_player}')
    if is_player1_win:
      player1_deck += [player1_card, player2_card]
    else:
      player2_deck += [player2_card, player1_card]
    player1_deck = player1_deck[1:]
    player2_deck = player2_deck[1:]
    i += 1
  # winner: whichever not empty
  winning_player_deck = player1_deck if player1_deck else player2_deck
  print(f'Game {state_depth + 1} over at round {i}: Player {1 if player1_deck else 2} won: {winning_player_deck}')
  del state[state_depth]
  return 'Player1' if player1_deck else 'Player2', winning_player_deck
# assert_equals(play_war(load_decks('input/22_TEST.txt')), [3, 2, 10, 6, 8, 5, 9, 4, 7, 1])
# assert_equals(score(play_war(load_decks('input/22_TEST.txt'))), 306)
assert_equals(play_war(load_decks('input/22_TEST_sm.txt'), is_part1=False), ('Player2', [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))
# assert_equals(play_war(load_decks('input/22_TEST.txt'), is_part1=False), ('Player2', [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))
# assert_equals(score(play_war(load_decks('input/22_TEST.txt'), is_part1=False)[1]), 291)

# print(f'part 1: winning player score: {score(play_war(load_decks("input/22_INPUT.txt"))[1])}')
# print(f'part 2: winning player score: {score(play_war(load_decks("input/22_INPUT.txt"), is_part1=False)[1])}')
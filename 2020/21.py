# https://adventofcode.com/2020/day/21
from typing import List, Dict, Set, Tuple
from collections import defaultdict
from pyutil.fileio import file_lines
from pyutil.testing import assert_equals
import re

def parse(line) -> Tuple[Set[str], Set[str]]: 
  if not (match := re.search('(.*) \(contains ([^\)]*)\)', line)): raise SystemError('Parse error:', line)
  ingredients, allergens = match.group(1), match.group(2)
  return (set(map(str.strip, ingredients.split(' '))), set(map(str.strip, allergens.split(', '))))

def find_allergy_ingredients(lines : List[str]) -> Dict[str, int]:
  ingredient_counts = defaultdict(int)
  allergen_to_ingredients = defaultdict(set)
  for (ingredients, allergens) in map(parse, lines):
    for allergen in allergens:
      # print(' {} in one of {}'.format(allergen, ingredients)) 
      allergen_to_ingredients[allergen] = ingredients if allergen not in allergen_to_ingredients else allergen_to_ingredients[allergen] & ingredients
    for ingredient in ingredients:
      ingredient_counts[ingredient] += 1
  # finalize when only 1 possibility
  while any(map(lambda v : len(v) > 1, allergen_to_ingredients.values())):
    for allerg in allergen_to_ingredients:
      if len(allergen_to_ingredients[allerg]) == 1:
        known_ingredient = list(allergen_to_ingredients[allerg])[0]
        known_allergen = allerg
        # print('{} contains {}'.format(known_ingredient, known_allergen))
        # strike this allergen from other foods
        for allerg1 in allergen_to_ingredients:
          if known_allergen == allerg1: continue
          # print("checking:", allerg1)
          # print("checking:", allergen_to_ingredients[allerg1])
          if known_ingredient in allergen_to_ingredients[allerg1]: 
            allergen_to_ingredients[allerg1].remove(known_ingredient)

  allergen_incredients = set()
  for allergen in allergen_to_ingredients:
    allergen_incredients |= allergen_to_ingredients[allergen]
  sum_allergen_free_ingredient_counts = sum(cnt for ingred, cnt in ingredient_counts.items() if not ingred in allergen_incredients)

  # print("counts:", ingredient_counts)
  # print("sum:", sum_allergen_free_ingredient_counts)
  allergen_incredients = dict( (key, list(value)[0]) for key, value in allergen_to_ingredients.items() )
  return allergen_incredients, sum_allergen_free_ingredient_counts
assert_equals(find_allergy_ingredients(file_lines('2020/input/21_TEST.txt')), ( {'dairy': 'mxmxvkd', 'fish': 'sqjhc', 'soy': 'fvjkl'}, 5))

def dangerous_ingredients(allergen_to_ingredient):
  return ','.join([allergen_to_ingredient[allerg] for allerg in sorted(allergen_to_ingredient)])

# number of times allergy free incredients appear in entire list
# allergen_incredients, count = find_allergy_ingredients(load_file('input/21_TEST.txt'))
allergen_incredients, count = find_allergy_ingredients(file_lines('2020/input/21_INPUT.txt'))
print('part1: count allergy free ingredients:', count)
print("part2: dangerous ingredients: '{}'".format(dangerous_ingredients(allergen_incredients)))

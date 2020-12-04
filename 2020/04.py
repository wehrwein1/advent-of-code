from typing import List
import re

# https://adventofcode.com/2020/day/4
lines = [line for line in map(str.rstrip, open('input/04_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/04_TEST.txt'))]
# lines = [line for line in map(str.rstrip, open('input/04_TEST_INVALID.txt'))]
# lines = [line for line in map(str.rstrip, open('input/04_TEST_VALID.txt'))]
print('input (len={}): {}'.format(len(lines), lines))

required_fields = ['byr', 'iyr', 'eyr', 'hgt','hcl','ecl','pid']
optional_fields = ['cid']

def all_required_fields_present(passport, required_fields):
  return all([required_field in passport for required_field in required_fields])

def all_required_fields_valid(passport, required_fields):
  if not all_required_fields_present(passport, required_fields): return False
  # print(" start detailed checking")
  def is_valid_height(value):
    height = value[:-2]                                                       # a number followed by either cm or in
    if value.endswith("cm"): return int(height) >=150 and int(height) <= 193  # If cm, the number must be at least 150 and at most 193.
    if value.endswith("in"): return int(height) >=59 and int(height) <= 76    # If in, the number must be at least 59 and at most 76.
    raise SystemError("Unhandled height", value)
  def is_valid_birth_year(value): return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002    # four digits; at least 1920 and at most 2002 
  def is_valid_issue_year(value): return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020    # four digits; at least 2010 and at most 2020
  def is_valid_exp_year(value):   return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030    # four digits; at least 2020 and at most 2030
  def is_valid_hair_color(value): return len(value) == 7 and bool(re.match('#[a-f0-9]{6}',value))         # a '#' followed by exactly six characters 0-9 or a-f
  def is_valid_eye_color(value):  return value in ['amb','blu','brn','gry','grn','hzl','oth']             # exactly one of: amb blu brn gry grn hzl oth.
  def is_valid_passport_id(value):return len(value) == 9 and int(value) <= 999999999
  field_validators = { 'byr' : is_valid_birth_year, 
                       'iyr' : is_valid_issue_year,
                       'eyr' : is_valid_exp_year, 
                       'hgt' : is_valid_height,
                       'hcl' : is_valid_hair_color, 
                       'ecl' : is_valid_eye_color,
                       'pid' : is_valid_passport_id }
  # some quick checks, proper pytest would be better
  assert is_valid_birth_year('1920'); is_valid_birth_year('2002'); assert not is_valid_birth_year('2003')
  assert is_valid_issue_year('2010'); is_valid_issue_year('2020'); assert not is_valid_issue_year('2009'); assert not is_valid_issue_year('2021')
  assert is_valid_exp_year('2020'); is_valid_exp_year('2030'); assert not is_valid_exp_year('2019'); assert not is_valid_exp_year('2031'); assert not is_valid_exp_year('11')
  assert is_valid_height('60in'); assert is_valid_height('190cm'); assert not is_valid_height('190in')
  assert is_valid_hair_color('#123abc'); assert not is_valid_hair_color('#123abz'); assert not is_valid_hair_color('123abc'); assert not is_valid_hair_color('#1234abc')
  assert is_valid_eye_color('brn'); assert not is_valid_eye_color('wat'); assert not is_valid_eye_color('oth1')
  assert is_valid_passport_id('000000001'); assert not is_valid_passport_id('0123456789'); 

  for field, value in passport.items():
    # print('  checking', field, value)
    try:
      if field in optional_fields: continue # skip validation
      if not field_validators[field](value): 
        # print('  checked field:', field, value, '-> invalid')
        return False
      # print('  checked field:', field, value, '-> valid')
    except Exception as e:
      # print("Exception for field", field, "->", e)
      return False 
  return True # valid passport

def parse_passports(lines : List[str]):
  i = 0
  passports = []
  while i < len(lines):  
    line = lines[i]
    passport = dict()
    while not len(line) == 0:
      # print('line {}: {}'.format(i, line))
      records = line.split(' ')
      # print(' records:', records)
      fields_present = [record.split(':') for record in records]
      # print(' fields_present:', fields_present)
      for key, value in fields_present:
        passport[key] = value
      i += 1
      line = lines[i] if i < len(lines) else '' # advance inner loop
    passports.append(passport)
    i += 1
  return passports

passports = parse_passports(lines)
valid_passports_count : int = 0
for passport in passports:
  is_valid_passport = all_required_fields_present(passport, required_fields)
  # is_valid_passport = all_required_fields_valid(passport, required_fields)
  print('checking passport: {} -> {}'.format(passport, is_valid_passport))
  if is_valid_passport: valid_passports_count += 1
print('valid_passports_count:', valid_passports_count)
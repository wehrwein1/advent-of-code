from day04 import is_valid_birth_year, is_valid_issue_year, is_valid_exp_year, is_valid_height, is_valid_hair_color, is_valid_eye_color, is_valid_passport_id

def test_is_valid_birth_year():
  assert is_valid_birth_year('1920')
  assert is_valid_birth_year('2002')
  assert not is_valid_birth_year('2003')

def test_is_valid_issue_year():
  assert is_valid_issue_year('2010')
  assert is_valid_issue_year('2020')
  assert not is_valid_issue_year('2009')
  assert not is_valid_issue_year('2021')

def test_is_valid_exp_year():
  assert is_valid_exp_year('2020')
  assert is_valid_exp_year('2030')
  assert not is_valid_exp_year('2019')
  assert not is_valid_exp_year('2031')
  assert not is_valid_exp_year('11')

def test_is_valid_height():
  assert is_valid_height('60in')
  assert is_valid_height('190cm')
  assert not is_valid_height('190in')

def test_is_valid_hair_color():
  assert is_valid_hair_color('#123abc')
  assert not is_valid_hair_color('#123abz')
  assert not is_valid_hair_color('123abc')
  assert not is_valid_hair_color('#1234abc')

def test_is_valid_eye_color():
  assert is_valid_eye_color('brn')
  assert not is_valid_eye_color('wat')
  assert not is_valid_eye_color('oth1')

def test_is_valid_passport_id():
  assert is_valid_passport_id('000000001')
  assert not is_valid_passport_id('0123456789')

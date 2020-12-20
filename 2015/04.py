# https://adventofcode.com/2015/day/4
from hashlib import md5

def find_adventcoin(secret_key : str, match_prefix : str) -> int:
  i = 0
  while True:
    if md5(str(secret_key + str(i)).encode('utf-8')).hexdigest().startswith(match_prefix):
      return i
    i+= 1

print('part 1: first adventcoin (5 zeros):', find_adventcoin(secret_key='ckczppom', match_prefix='0' * 5))
print('part 2: first adventcoin (6 zeros):', find_adventcoin(secret_key='ckczppom', match_prefix='0' * 6))

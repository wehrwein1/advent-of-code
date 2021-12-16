from functools import reduce
from typing import List

def product(numbers : List[int]):
  return reduce(lambda x, y: x * y, numbers)
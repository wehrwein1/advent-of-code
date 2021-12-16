from typing import List

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
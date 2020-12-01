# https://adventofcode.com/2020/day/1
# Part 1: 2SUM
# Part 2: 3SUM
entries = list(map(int, [line for line in map(str.rstrip, open('input/01_INPUT.txt'))]))
print(entries)
for i in range(len(entries)):
  for j in range(len(entries)):
    for k in range(len(entries)):
      if entries[i] + entries[j] + entries[k] == 2020:
        print("mult=", entries[i] * entries[j] * entries[k])
        exit()
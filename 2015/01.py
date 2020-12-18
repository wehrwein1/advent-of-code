# https://adventofcode.com/2015/day/1
steps = open('input/01_INPUT.txt').readline()
UP, DOWN = '(', ')'
print('part 1: Santa ends on floor:', steps.count(UP) - steps.count(DOWN))
floor = 0
i = 0
while floor >= 0:
  delta = 1 if steps[i] == UP else -1
  floor += delta
  i += 1
print('part 2: Santa first goes to basement on step:', i)

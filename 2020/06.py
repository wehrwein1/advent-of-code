# https://adventofcode.com/2020/day/6
from typing import List


lines = [line for line in map(str.rstrip, open('input/06_INPUT.txt'))]
# lines = [line for line in map(str.rstrip, open('input/06_TEST.txt'))]
print('input (len={}): {}'.format(len(lines), lines))
# print('input (len={})'.format(len(lines)))



# boarding_groups = dict()
question_counts = []
i : int = 0
while i < len(lines):  
    line = lines[i]
    group_questions = set()
    while not len(line) == 0:
      group_questions |= set(list(line))
      i += 1
      line = lines[i] if i < len(lines) else '' # advance inner loop
    count = len(group_questions)
    print('group={}, sum_questions={}'.format(group_questions, count))
    print("question_counts:", question_counts)
    question_counts.append(count)
    i += 1

print("sum counts:", sum(question_counts))

import collections

d = collections.defaultdict(int)
d[0] = 1
sum = 0;
while True:
	for line in open('input/01_INPUT.txt'):
		sum += int(line)
		if sum in d:
			print("first match", sum)
			quit()
		print("line=", int(line))
		d[sum] += 1
print("finished?")


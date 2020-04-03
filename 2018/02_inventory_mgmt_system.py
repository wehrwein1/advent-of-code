double_letters = 0
triple_letters = 0
lines = [line for line in open('input/02_INPUT.txt')]

# approach: 
# - compute a unique number for each
# - sort results then find similar numbers and check manually

length = len(lines)
for i,line1 in enumerate(lines):
	for j in range(i+1, length):
		line2 = lines[j]
		diff = 0
		print("lines({},{})=[{},{}]".format(i,j,line1.rstrip(),line2.rstrip()))
		for k,char in enumerate(line1):
			print(" k={} '{}' and '{}'".format(k, line1[k],line2[k]))
			if line1[k] != line2[k]:	
				diff += 1
				if diff > 1: 
					print(" no match")
					break
		if diff == 1:
			print("diff=", diff)
			print(line1.rstrip())
			print(line2.rstrip())
			quit()
print("found no match")
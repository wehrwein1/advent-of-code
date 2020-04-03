instructions = [list(map(int, line.split(','))) for line in map(str.rstrip, open('input/02_INPUT.txt'))][0]

def compute_opcode_zero(op_codes, noun, verb):
	op_codes[1]=noun
	op_codes[2]=verb
	index = 0
	print("Trying noun:", noun, "verb:", verb, "op_codes:", op_codes)
	while (True):
		operation = op_codes[index]
		#print("  operation", operation)
		if (operation == 99):
			break
		elif (operation == 1):
			op_codes[op_codes[index+3]] = op_codes[op_codes[index+1]] + op_codes[op_codes[index+2]]
		elif (operation == 2):
			op_codes[op_codes[index+3]] = op_codes[op_codes[index+1]] * op_codes[op_codes[index+2]]
		else:
			raise SystemError(operation) 
		index +=4
	#print(" op_codes final", op_codes)
	return op_codes[0]

for noun in range(100):
	for verb in range(100):
		result = compute_opcode_zero(list(instructions), noun, verb)
		print("noun:", noun, "verb:", verb, "result:", result)
		if (result == 19690720):
			raise SystemError("found it", 100 * noun + verb) 
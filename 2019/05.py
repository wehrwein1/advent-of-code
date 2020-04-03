import collections
from enum import Enum
instructions = [list(map(int, line.split(','))) for line in map(str.rstrip, open('input/05_INPUT.txt'))][0]

#instructions = [1002,4,3,4,33]

print(instructions)

class Operation(Enum):
	ADD = 1
	MULTIPLY = 2
	SET_VALUE = 3
	PRINT_VALUE = 4
	QUIT = 99
	def describe(self):
		return self.name, self.value
	def __str__(self):
		return '{0}({1})'.format(self.name, self.value)
	def length(self): # total instruction length
		if self == Operation.ADD or self == Operation.MULTIPLY:
			return 4
		elif self == Operation.SET_VALUE:
			return 3
		elif self == Operation.PRINT_VALUE:
			return 1
		raise SystemError("unknown operation")

def parse_instruction(instruction):
	return instruction % 100, (instruction / 100) % 10, (instruction / 1000) % 10, (instruction / 10000) % 10

def run_opcodes(op_codes):
	#op_codes[1]=noun
	#op_codes[2]=verb
	i = 0
	(op, mode1, mode2, mode3) = parse_instruction(op_codes[i])
	print(op_codes[i], "->", (op, mode1, mode2, mode3))
	position_mode_value = lambda i : op_codes[op_codes[i]]
	immediate_mode_value = lambda i : op_codes[i]
	lookup_value = [position_mode_value, immediate_mode_value]
	while (True):
		operation = Operation(op)
		if operation == Operation.QUIT:
			break
		elif operation == Operation.ADD:
			op_codes[op_codes[i+3]] = lookup_value[mode1](i+1) + lookup_value[mode2](i+2)
		elif operation == Operation.MULTIPLY:
			op_codes[op_codes[i+3]] = lookup_value[mode1](i+1) * lookup_value[mode2](i+2)
		elif operation == Operation.SET_VALUE:
			op_codes[op_codes[i+2]] = lookup_value[mode1](i+1)
		elif operation == Operation.PRINT_VALUE:
			print(op_codes[i+1])
		else:
			raise SystemError(operation) 
		i += operation.length()
	#print(" op_codes final", op_codes)
	return op_codes[0]

run_opcodes(instructions)
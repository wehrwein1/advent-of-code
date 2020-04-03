masses = map(int, [line for line in map(str.rstrip, open('input/01_INPUT.txt'))])

def fuel_for_mass(mass):
	return int(mass/3)-2

sum = 0
for mass in masses:
	remaining_mass = mass
	print("mass", mass)
	while (remaining_mass > 0):
		fuel = fuel_for_mass(remaining_mass)
		if (fuel <= 0):
			break
		sum += fuel
		remaining_mass = fuel
		print("* remaining_mass", remaining_mass)
print("sum", sum)
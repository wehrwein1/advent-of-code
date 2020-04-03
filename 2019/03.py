import collections
import sys

instructions = [line.split(',') for line in map(str.rstrip, open('input/03_INPUT.txt'))]

coord_state = collections.defaultdict(lambda : collections.defaultdict(lambda : sys.maxsize)) # (x,y) -> dict(user, step_count)

print("instructions", instructions)

def get_next_position(x_y, dir):
	if (dir == "R"):
		return (x_y[0]+1, x_y[1])
	elif (dir == "D"):
		return (x_y[0], x_y[1]-1)
	elif (dir == "U"):
		return (x_y[0], x_y[1]+1)
	elif (dir == "L"):
		return (x_y[0]-1, x_y[1])
	raise SystemError("not impl:", dir)

def walk(instructions, user):
	print("walking for", user, instructions)
	(x,y)=(0,0)
	steps = 0
	for instruction in instructions:
		dir = instruction[0]
		walk_steps = int(instruction[1:])
		print("instruction:", instruction, dir, walk_steps)
		for i in range(walk_steps):
			(x,y) = get_next_position((x,y), dir)
			steps += 1
			#print("next: ", (x,y))
			if steps < coord_state[(x,y)][user]:
				coord_state[(x,y)][user] = steps
	
walk(instructions[0], "user1")
walk(instructions[1], "user2")

	
#code_counts = collections.defaultdict(int)

#print("\ncoord_state:", coord_state)
overlaps = dict(filter(lambda kv: len(kv[1]) == 2, coord_state.items()))
print("\noverlaps:", overlaps)

min_coord = min(overlaps, key=(lambda k : sum(overlaps[k].values())))
print("min_coord", min_coord)
print("min sum", sum(overlaps[min_coord].values()))
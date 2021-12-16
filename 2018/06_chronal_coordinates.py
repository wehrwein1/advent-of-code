import string

def print_grid(grid):
	#print(grid)
	for row in grid:
		print(*row, sep=' ')

def get_code(index):
	if index < 26:
		return string.ascii_uppercase[index]
	if index < 2*26:
		return 'A' + get_code(index % 26)
	raise SystemError("unhandled index" + i)

coords = [list(map(int, line.split(', '))) for line in map(str.rstrip, open('input/06_INPUT.txt'))]
dim = max(map(lambda row : max(row), coords))
print("dim=", dim)
grid = [[0] * (dim+1) for _ in range(dim+1)]
#print_grid(grid)
for coord in coords:
	print("{}".format(coord))
	
for i,(x,y) in enumerate(coords):
	print("i={}, coords=({},{}), code='{}'".format(i,x,y, get_code(i)))
	grid[x][y] = get_code(i)
#print_grid(grid)
	
def manhattan_distance(p1, p2):
	return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

def find_nearest_code(grid_point, coords):
	code_to_distance = { grid[x][y] : manhattan_distance(grid_point, (x,y)) for (x,y) in coords }
	min_distance = min(code_to_distance.values())
	codes = list(filter(lambda key : code_to_distance[key]==min_distance, code_to_distance))
	result = "." if len(codes) > 1 else codes[0].lower()
	print("find_nearest_code({},{})='{}'".format(grid_point[0], grid_point[1], result))
	return result

def is_sum_distance_under_threshold(grid_point, coords, threshold=10000):
	code_to_distance = { grid[x][y] : manhattan_distance(grid_point, (x,y)) for (x,y) in coords }
	#print("{} -> {} sum={}".format(grid_point, code_to_distance, sum(code_to_distance.values())))
	return sum(code_to_distance.values()) < threshold
	
#print(manhattan_distance((0,0), (1,2)))
#print(find_nearest_code((0,0),coords))

marked_coords = list()
for i,row in enumerate(grid):
	for j,cell in enumerate(row):
		#if grid[i][j] == 0:
			if is_sum_distance_under_threshold((i,j), coords):
				marked_coords += [(i,j)]
			#grid[i][j] = find_nearest_code((i,j), coords)
for tuple in marked_coords:
	grid[tuple[0]][tuple[1]] = '#'
#print_grid(grid)

#infinite_codes = sorted(set(grid[0] + grid[dim] + [grid[i][0] for i in range(dim+1)] + [grid[0][i] for i in range(dim+1)]))
#infinite_codes = sorted(map(lambda code : code.lower(), infinite_codes))
#print("infinite_codes=", infinite_codes)

#code_counts = collections.defaultdict(int)
safe_regions_count = 0
for i,row in enumerate(grid):
	for j,cell in enumerate(row):
		code = grid[i][j]
#		if not code.lower() in infinite_codes:
#			code_counts[code.lower()] += 1
		if code == '#':
			safe_regions_count += 1
#			
#print("code_counts=", code_counts)
#max_value = max(code_counts.values())
#print("size of largest area={} (code: '{}')".format(max_value, None))
print("safe_regions_count=", safe_regions_count)


import time

class Claim:
	id = 0
	x,y = -1,-1
	width,height= 0,0
	text = None
	def __init__(self, text):
		tokens = text.split(' ')
		self.id = int(tokens[0].lstrip('#'))
		xy = [int(token) for token in tokens[2].rstrip(':').split(',')]
		dim = [int(token) for token in tokens[3].split('x')]
		self.x,self.y = xy[0], xy[1]
		self.width,self.height= dim[0], dim[1]
		self.text = text
	def __str__( self ):
		return self.text
		
fabric_size = 1000
def has_overlap(claim1, claim2):
	fabric = [[0 for i in range(fabric_size)] for j in range(fabric_size)]
	return mark_claim(claim1, fabric) or mark_claim(claim2, fabric)
	
def mark_claim(claim, fabric):
	for x1 in range(claim.x, claim.x + claim.width):
		for y1 in range(claim.y, claim.y + claim.height):
			if fabric[x1][y1] > 0:
				return True # found overlap
			fabric[x1][y1] = claim.id
	return False			
		
claim_lines = [claim for claim in map(str.rstrip, open('input/03_INPUT.txt'))]
#claim_lines = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
claims = map(lambda text : Claim(text), claim_lines)
claims_map = { key: value for (key, value) in map(lambda claim : (claim.id, claim), claims) }

found_overlaps = set() 							# claim ids which have any overlap
non_overlaps = collections.defaultdict(set) 	# (key,value) = (min id, set of non-overlapping max ids)
start_time = time.time()
for i in range(1, len(claim_lines)+1):
	claim1 = claims_map[i]
	print("Checking:", str(claim1))
	if claim1.id in found_overlaps:
		continue # check next claim1
	found_overlap = False
	for j in range (i, len(claim_lines)+1): # +1 to avoid identity comparisons and improve performance
		claim2 = claims_map[j]
		if i == j: continue # skip self
		if claim2.id in found_overlaps:
			found_overlap = True
			continue # has overlaps with something, check next claim2
		if claim2.id in non_overlaps[claim1.id]:
			continue # we already know it doesn't overlap, check next claim2
		print(" checking: {} / {}".format(claim1.id, str(claim2)))
		if has_overlap(claim1, claim2):
			found_overlaps.update([claim1.id, claim2.id])
			print(" Found overlap: {},{} -> {}".format(i,j, found_overlaps))
			found_overlap = True
			break # check next claim2
		non_overlaps[claim1.id].add(claim2.id)
	if not found_overlap:
		print("Has no overlap: '{}'".format(claim1)) 
		elapsed_time = time.time() - start_time
		print('elapsed_time', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
		quit()
print("found no non-overlapping claims (error?)")	
elapsed_time = time.time() - start_time
print('elapsed_time', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
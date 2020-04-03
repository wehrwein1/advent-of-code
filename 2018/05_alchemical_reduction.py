import sys
import string
import collections

ascii_delta = ord('a') - ord('A')
def remove_reacting_polymers(polymers):
	# print "delta=", ascii_delta
	removed_indices = set()
	for i in range(0, len(polymers)-1):
		if i in removed_indices:
			continue
		if abs(ord(polymers[i+1])-ord(polymers[i])) == ascii_delta:
			#print "skipping ({},{})={}{}".format(i, i+1, polymers[i], polymers[i+1])
			removed_indices.update([i, i+1])
	#print "removed_indices=", removed_indices
	buffer = ""
	for i, char in enumerate(polymers):
		if i not in removed_indices:
			buffer += char
	return buffer
	
min_final_length = sys.maxsize
most_reactant_polymer = None
for c in list(string.ascii_lowercase):
	polymers = [line for line in open('input/05_INPUT.txt')][0].rstrip()
	#polymers = 'dabAcCaCBAcCcaDA'
	if not c in polymers:
		continue
	remove_chars = [c, chr((ord(c)-ascii_delta))]
	#print("polymers(len={})='{}'".format(len(polymers),polymers))
	print(" remove_chars=", remove_chars)
	
	# remove remove_chars
	polymers = ''.join( c for c in polymers if c not in remove_chars)
	#print(" polymers removed(len={})='{}'".format(len(polymers),polymers))
		
	#print "polymers (init)=", polymers
	last_length = -1
	while len(polymers) != last_length:
		last_length = len(polymers)
		polymers = remove_reacting_polymers(polymers)
		#print "polymers (iter)=", polymers

	#print(" polymers(len={})='{}'".format(len(polymers),polymers))
	if len(polymers) < min_final_length:
		min_final_length = len(polymers)
		most_reactant_polymer = c
		
print("\nmin_final_length=", min_final_length)
print("most_reactant_polymer=", most_reactant_polymer)
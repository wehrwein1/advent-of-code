import sys
import collections

records = sorted([record for record in map(str.rstrip, open('input/04_INPUT.txt'))])

def is_guard_change(record):
	return int(record.split('#')[1].split(' ')[0]) if 'Guard' in record else -1
	
guard_sleep = collections.defaultdict(lambda : [0] * 60)
guard_sums = collections.defaultdict(int)

guard_id = -1
fell_asleep_time = None
for record in records:
	print(record)
	if is_guard_change(record) > 0:
		#print("  guard:", is_guard_change(record))
		guard_id = is_guard_change(record)
	if 'falls asleep' in record:
		fell_asleep = record.split(' ')[1].rstrip(']').split(':')[1]
		#print("  fell asleep", fell_asleep)
	elif 'wakes up' in record:
		woke_up = record.split(' ')[1].rstrip(']').split(':')[1]
		total = int(woke_up)-int(fell_asleep)
		print("** guard {} slept from {}-{} ({} total)".format(guard_id, fell_asleep, woke_up, total))
		for min in range(int(fell_asleep), int(woke_up)):
			guard_sleep[guard_id][min] += 1
		guard_sums[guard_id] += total

max_freq = -1
max_guard_id = -1		
for guard_id in guard_sleep:
	print(guard_id, *guard_sleep[guard_id], sep=" ")
	if max(guard_sleep[guard_id]) > max_freq:
		max_freq = max(guard_sleep[guard_id])
		max_guard_id = guard_id
	
max_minute = guard_sleep[max_guard_id].index(max_freq)
#print("sums by guard id", guard_sums)		
#(max_guard_id,max_slept) = max(guard_sums.items(), key=lambda item : item[1])
#max_minute = guard_sleep[max_guard_id].index(max(guard_sleep[max_guard_id]))

print("guard:", max_guard_id)
#print("max_slept:", max_slept)
#print("sleep:", *guard_sleep[max_guard_id], sep=" ")
print("max_minute:", max_minute)
print("result=", max_guard_id*max_minute)
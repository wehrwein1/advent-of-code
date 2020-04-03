import string
import sys
import collections

line = '171309-643603'
(low,high) = map(int, line.split('-')) #assumed inclusive
print(low,high)
passwords = []

def is_password(number):
	has_adjacent_same_digits = False
	digits = str(number)
	for i,char in enumerate (digits):
		#print("checking char", char, i)
		if not has_adjacent_same_digits and i > 0 and char == digits[i-1]:
			if char * 3 not in digits:
				has_adjacent_same_digits = True
				continue
		if i > 0 and int(char) < int(digits[i-1]):
			#print("found decreasing\n")
			return False
	is_password = has_adjacent_same_digits
	print("finished checking", number, "has_adjacent_same_digits:", has_adjacent_same_digits, "-->", is_password, "\n")
	return is_password

passwords = list(filter(is_password, range(low, high)))
print("passwords:", passwords)
print("count:", len(passwords))

is_password(112233)
is_password(123444)
is_password(111122)
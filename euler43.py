__author__ = 'ahalbert'

import itertools

def isPandigital(n):
	if not n%3 == 0:
		return False
	digits = "0123456789"
	n = str(n)
	digits = digits[:len(n)]
	for i in digits:
		if i not in n:
			return False
	return True


def hasPandigitalProperty(n):
	n = str(n)
	primes = [2,3,5,7,11,13,17]
	index = 1
	for i in primes:
		if not int(n[index]+n[index+1]+n[index+2]) % i == 0:
			return False
		index += 1
	return True

def euler43():
	s = 0
	for i in itertools.permutations("0123456789"):
		temp = "".join(i)
		if temp[0] != '0':
			if hasPandigitalProperty(temp):
				s += int(temp)
	return s
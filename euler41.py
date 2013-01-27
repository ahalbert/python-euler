__author__ = 'ahalbert'

from euler7 import findPrimes

def isPandigital(n):
	digits = "123456789"
	n = str(n)
	digits = digits[:len(n)]
	for i in digits:
		if i not in n:
			return False
	return True

def euler41():
	largest = 0
	for i in findPrimes(9999999):
		if isPandigital(i):
			print i
			largest = i
	return largest
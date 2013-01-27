__author__ = 'ahalbert'

from euler7 import *

def LeftRightTruncate(s):
	return s[1:]

def RightLeftTruncate(s):
	return s[:-1]

def isTruncatblePrime(s):
	left = s
	right = s
	if len(s) == 1:
		return False
	for i in xrange(len(s)-1):
		left = LeftRightTruncate(left)
		right = RightLeftTruncate(right)
		if not (isPrime(int(left)) and  isPrime(int(right))):
			return False
	return True

def euler35():
	addi = 0
	for n in findPrimes(10000000):
		if isTruncatblePrime(str(n)):
			addi = addi + n
			print n
	return addi
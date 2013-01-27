__author__ = 'ahalbert'

from euler7 import *

def rotate(s):
	return s[-1]+s[:-1]

def isCircular(n):
	circular = str(n)
	for s in xrange(len(circular)):
		permu = int(circular)
		if not isPrime(permu):
			return False
		circular = rotate(circular)
	return True
	

def euler34():
	isCircular(197)
	result = 0
	for i in findPrimes(1000000):
		if isCircular(i):
			print i
			result = result + 1
	return result
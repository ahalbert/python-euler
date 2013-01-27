__author__ = 'ahalbert'

from euler7 import isPrime



def euler27():
	maxConsecutives = 0
	maxa = 0
	maxb = 0
	for a in xrange(-999,1000):
		for b in xrange(-999,1000):
			temp = computeConsecutivePrimes(a,b)
			if temp > maxConsecutives:
				maxConsecutives,maxa,maxb = temp,a,b
	return maxa*maxb

def computeConsecutivePrimes(a, b):
		x = 0
		eval = x*x + a*x + b
		while eval > 0 and isPrime(eval):
			eval = x*x + a*x + b
			x += 1
		return x


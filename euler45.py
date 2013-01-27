__author__ = 'ahalbert'

from math import sqrt

def isPentagonal(x):
	f = (.5 + sqrt(.25+6*x))/3
	if f - int(f) == 0:
		return True
	return False



def isTriangle(x):
	f = .5*(-1+sqrt(8*x+1))
	if f - int(f) == 0:
		return True
	return False

def generateHexagonal(n):
	hexagonals = []
	for i in xrange(1,n+1):
		hexagonals.append(i*((2*i)-1))
	return hexagonals

def euler45():
	hexagonals = generateHexagonal(200000)
	hexagonals = hexagonals[143:]
	for i in hexagonals:
		if isPentagonal(i):
			if isTriangle(i):
				return i
	return None
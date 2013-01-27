__author__ = 'ahalbert'


from euler7 import  findPrimes
import itertools

def areSameDistance(a,b,c):
	if c-b == b-a:
		return True
	return False

def euler49():
	primes = []
	loc = []
	locvalues = []
	for i in findPrimes(100000):
		if len(str(i)) == 4:
			primes.append(i)
	for i in primes:
		for j in itertools.permutations(str(i)):
			j = int("".join(j))
			if j != i and j % 2 != 0 and j not in locvalues and j in primes:
				loc.append(primes.index(j))
				locvalues.append(j)
		if len(loc) == 3 and areSameDistance(locvalues[0],locvalues[1],locvalues[2]):
			return "" + str(locvalues[0]) + str(locvalues[1]) + str(locvalues[2])
		for k in locvalues:
			primes.remove(k)
		loc = []
		locvalues = []
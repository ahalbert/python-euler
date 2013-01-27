__author__ = 'ahalbert'

from euler7 import findPrimes


def consecutiveSums(primes,total,limit):
	pos = limit
	bottomSum = total
	topSum = total
	while topSum not in primes and pos > -1:
		topSum -= primes[pos]
		pos -= 1
	pos = 0
	while bottomSum not in primes and bottomSum > 0:
		bottomSum -= primes[pos]
		pos += 1
	if topSum not in primes:
		topSum = 0
	if bottomSum not in primes:
		bottomSum = 0
	print topSum,",",bottomSum
	return max(bottomSum,topSum)

def euler50():
	primes = []
	total = 0
	pos = 0
	limit = 0
	largest  = 0
	for i in findPrimes(1000000):
		if i < 1000000:
			primes.append(i)
	while total < 1000000:
		total += primes[pos]
		pos += 1
	pos -= 1
	total -= primes[pos]
	limit = pos
	while limit < len(primes) - 1:
		temp = consecutiveSums(primes,total,limit)
		if temp > largest:
			largest = temp
			print largest
		limit += 1
		total += limit
		pos = 0
		while total > 1000000:
			total -= primes[0]
			primes = primes[1:]
			limit -= 1
	return largest
__author__ = 'ahalbert'

import prime
from euler7 import findPrimes

persist = {}
primePointer = [0]

def primeFactors(n,prev,primes):
	if n == primes[primePointer[0]]:
		persist[n] = [n]
		primePointer[0] += 1
		return []
	original = n
	factors = []
	pos = 0
	for i in prev:
		if n % i == 0:
			return []
	while n != 1:
		while n % primes[pos] == 0:
			n /= primes[pos]
			if primes[pos] not in factors:
				factors.append(primes[pos])
			if n in persist:
				for m in persist[n]:
					if m not in factors:
						factors.append(m)
				n = 1
		pos += 1
	if n != 1 and n < 800000:
		persist[original] = factors
	if len(factors) != 4:
		return []
	return factors


def removeDuplicate(l):
	nl = []
	for i in l:
		if i not in nl:
			nl.append(i)
	return nl

def euler47():
	p = prime.Prime()
	primes = []
	for i in findPrimes(1000000):
		primes.append(i)
	factors = []
	seq = []
	n = 1
	while len(seq) != 4:
		seq.append(n)
		temp = primeFactors(n,factors,primes)
		if n >= 134043 and n< 134047:
			print n,":",temp
		if len(temp) == 4:
			print n
			factors += temp
			n += 1
		else:
			n = seq[0]+1
			seq = []
			factors = []
	return seq

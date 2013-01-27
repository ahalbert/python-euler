from euler7 import findPrimes

__author__ = 'ahalbert'



def findFamilySize(p,primes):
	family = []
	if len(str(p)) == 1:
		return []
	p = str(p)
	temp = ""
	for i in xrange(len(p)):
		for j in xrange(i+1,len(p)):
			for k in "1234567890":
				temp = p[:i] + k + p[i+1:j] + k + p[j+1:]
				if int(temp) in primes and int(temp) not in family and len(str(int(temp))) == len(p):
					family.append(temp)
				if len(family) == 8:
					print  family
					return family
			family = []
	return family

def euler51():
	primes = []
	for i in findPrimes(1000000):
		primes.append(i)
	findFamilySize(157,primes)
	for i in primes:
		if len(findFamilySize(i,primes)) == 8:
			return i
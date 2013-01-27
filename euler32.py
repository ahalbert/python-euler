__author__ = 'ahalbert'

def isPandigital(a,b):
	#print a
	#print b
	digits = [False]*9
	sa = str(a)
	sb = str(b)
	product = str(a*b)
	if not (len(sa) + len(sb) + len(product) == 9):
		return False
	if "0" in sa or "0" in sb or "0" in product:
		return False
	for i in sa:
		digits[int(i)-1] = True
	for i in sb:
		digits[int(i)-1] = True
	for i in product:
		digits[int(i)-1] = True
	if False in digits:
		return False
	else:
		return True

def euler32():
	sm = 0
	pandigitals = []
	for i in xrange(0,10000):
		for j in xrange(0,10000):
			if	i*j not in pandigitals:
				if isPandigital(i,j):
					sm += i*j
					pandigitals.append(i*j)
					print i, " ", j, " ", i*j
	print sm
	return sum(pandigitals)


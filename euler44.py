__author__ = 'ahalbert'


def generatePentagonal(n):
	pentagonals = []
	for i in xrange(1,n+1):
		pentagonals.append((i*(3*i-1))/2)
	return pentagonals

def hasPentagonalPair(j,pentagonals,index):
	subpentagonals = pentagonals[:index]
	for k in subpentagonals:
		if j-k in pentagonals and j+k in pentagonals:
			return k
	return None


def euler44():
	minimal = 0
	minimalPair = (1,5)
	k = 0
	pentagonals = generatePentagonal(5000)
	for j in pentagonals:
		k  = hasPentagonalPair(j,pentagonals,pentagonals.index(j))
		if k != None:
			if abs(j-k) < minimal:
				minimal = min(abs(j-k),abs(k-j))
				minimalPair = (j,k)
	print minimalPair
	return minimal
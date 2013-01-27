__author__ = 'ahalbert'

coins = [1,5,10,25,50,100,200]
table = {}

def computeTable(n,k):
	for i in xrange(n+1):
		for j in xrange(k+1):
			table[(i,j)] = combinations(i,j)
	return table

def combinations(n,k):
	if n == 0:
		return  1
	elif k < 1 or n < 0:
		return 0
	if (n,k-1) in table:
		a = table[(n,k-1)]
	else:
		a = combinations(n,k-1)
	if (n-coins[k],k) in table:
		b = table[(n-coins[k],k)]
	else:
		b = combinations(n,k-1)
	return a+b

def euler31():
	target = 200
	coins = [1,2,5,10,20,50,100,200]
	ways = [1]+[0]*target
	for coin in coins:
		for i in range(coin, target+1):
			ways[i] += ways[i-coin]
	return ways[target]
__author__ = 'ahalbert'

def cancel(numerator, denominator):
	didCancel = False
	if numerator % 10  == 0 and denominator % 10 == 0:
		return 0
	a = str(numerator)
	b = str(denominator)
	i = 0
	while i < len(a):
		for j in xrange(len(b)):
			if a[i] == b[j]:
				a = a[:i] + a[i+1:]
				b = b[:j] + b[j+1:]
				didCancel = True
				break
		i = i+1
	if b != '0' and didCancel == True:
		return float(a)/float(b)
	else:
		return 0

def euler33():
	for i in xrange(10,100):
		for j in xrange(19,100):
			if float(i)/float(j) < 1.0:
				x = float(i)/float(j)
				y = cancel(i,j)
				if float(i)/float(j) == cancel(i,j):
					print i,"/", j
					

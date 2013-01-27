__author__ = 'ahalbert'

def isPandigitalProduct(base):
	pandigital = ""
	mult = 1
	while len(pandigital) < 9:
		pandigital += str(base * mult)
		mult += 1
	if len(pandigital) != 9 or '0' in pandigital:
		return False
	for i in "123456789":
		if i not in pandigital:
			return False
	print base, ":",pandigital
	return True
			
	

def euler38():
	isPandigitalProduct(192)
	largest = 0
	for i in xrange(99999999):
		if isPandigitalProduct(i):

			largest = i
	return largest

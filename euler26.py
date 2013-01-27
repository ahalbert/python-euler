from decimal import *

def cyclelength(x):
	getcontext().prec = 2000
	floatingValue = Decimal(1)/Decimal(x)
	valuestring =str(floatingValue)
	length = 1
	pos = 0
	valuestring = valuestring[2:]
	teststring = ""
	for j in xrange(len(valuestring)):
		length = 2
		for i in xrange(1, len(valuestring)):
			a = valuestring[j:j+i+1]
			b = valuestring[j+i+1:j+i+i+2]
			if valuestring[j:j+i+1] == valuestring[j+i+1:j+i+i+2]:
				return length
			length = length + 1
	return length

def euler26():
	#for i in xrange(5,1000):
	#	print i, ":", 1.0/i
	print cyclelength(619)
	soln = 1
	solnvalue = 1
	for i in xrange(5,1000):
		temp = cyclelength(i)
		if temp > solnvalue or temp == 0:
			soln = i
			solnvalue = temp
	return soln
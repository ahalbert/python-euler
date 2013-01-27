__author__ = 'ahalbert'

def findDigit():
	digits = [1]
	dbase = [10,100,1000,10000,100000,1000000]
	base = [10,100,1000,10000,100000,1000000]
	length = 1
	baselength = 1
	concat = 1
	while base != []:
		if length == base[0]:
			digits.append(str(concat)[0])
			del base[0]
		if length > base[0]:
			digits.append(str(concat)[base[0]-length-1])
			del base[0]
		concat += 1
		if  concat >= dbase[0]:
			baselength += 1
			del dbase[0]
		length += baselength
	return digits

def euler40():
	product = 1
	digits = findDigit()
	for i in digits:
		product *= int(i)
	return product
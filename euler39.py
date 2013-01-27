__author__ = 'ahalbert'


def isSolution(a,b,c):
	if a*a + b*b == c*c:
		return True
	return False

def triangles(perimeter):
	solns = 0
	for c in xrange((perimeter/3)-1, (perimeter/2)+2):
		for b in xrange(1, (perimeter-c)+1):
			if isSolution((perimeter - b - c),b,c):
				solns += 1
	return solns

def euler39():
	longest = 0
	mostSolutions  = 0
	for i in xrange(1000):
		t = triangles(i)
		if t > mostSolutions:
			longest = i
			mostSolutions = t
	return longest
__author__ = 'ahalbert'

from math import sqrt

def isPrime( n ):
	if n == 1:
		return False
	if n == 2:
		return True
	elif n % 2 == 0:
		return False

	i = 3
	range = int(sqrt(n) ) + 1
	while( i < range ):
		if( n % i == 0):
			return 0
		i += 1
	return True


def findPrimes(x):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while q < x:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
__author__ = 'ahalbert'

import csv

def generateTriangles(n):
	triangles = []
	for i in xrange(1,n+1):
		triangles.append((i*(i+1))/2)
	return triangles

def decodeWord(s):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	value = 0
	for i in s:
		value += alphabet.find(i) + 1
	return value

def euler42():
	print decodeWord("SKY")
	words = 0
	triangles = generateTriangles(600)
	rfile = open("words.txt", "r")
	reader = csv.reader(rfile)
	for row in reader:
		for col in row:
			if decodeWord(col) in triangles:
				words += 1
	return words

  
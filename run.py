import os
import random

file = open("bingoSquaresHere.txt", "r")
haslastring = file.read()
haslalist = haslastring.split("\n")
haslalist.pop(-1)
if len(haslalist) < 25:
	print("I need more")
	exit()
for i in range(5):
	print("-----------------------------------------------------------------------------------------------")
	for j in range(5):
		index = random.randint(0, len(haslalist)) - 1
		print(" | ", haslalist[index], end=' ')
		haslalist.pop(index)
	print(' ')

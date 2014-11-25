#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

f = open("birds.txt", "r")
data = f.read()
f.close()

words = data.split(" ")
num_words = len(words)
lines = data.split("\n")
line_num = len(lines)
for l in lines:
	if not l:
		lines.remove(l)
line_num_fixed = len(lines)

print("The words in the text are: ", words)
print("The number of words is ", num_words)
print("The lines in the text are: ", lines)
print("Wrong: The number of lines is ", line_num)
print("Right: The number of lines is ", line_num_fixed)
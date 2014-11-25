#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
 
x = [5,10,15,20,25]

#init
y = []

for cnt in x:
	y.append(cnt/5)

print("\nOld fashioned way: x = {} y = {}\n".format(x,y))

z = [n/5 for n in x]

print("List Comprehensions: x= {} z = {} \n".format(x,z))

try:
	a = x /5
except Exception, e:
	print("No, you can't do that with regular python lists\n")

a = np.array(x)
b = a/5
print("With Numpy: a = {} b = {}\n".format(a, b))
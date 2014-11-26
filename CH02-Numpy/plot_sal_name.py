#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt

salary = np.fromfile("salaries.txt", dtype='int', sep=",")
names = np.genfromtxt("names.txt", dtype='str', delimiter=",")

x = np.arange(len(names))

plt.bar(x, salary)
plt.xticks(x, names)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

plt.show()
print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

salaries_new = salary[2:-2]
names_new = names[2:-2]
x = range(len(names_new))
plt.bar(x, salaries_new)
plt.xticks(x, names_new)
plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

plt.show()
print(np.max(salary), np.min(salary), np.average(salary), np.median(salary))

#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import numpy as np
import matplotlib.pyplot as plt

# create x, randomly spaced between 0 to 20
x = np.linspace(0,20,1000)

y1 = np.sin(x)
y2 = np.cos(x)

#Plot the sin and cos functions
plt.plot(x, y1, "-g", label="sin")
plt.plot(x, y2, "-b", label="cos")

#Legend top right
plt.legend(loc="upper right")

#Limit the y axis to -1.5 to 1.5
plt.ylim(-1.5, 1.5)
plt.show()

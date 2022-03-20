# Write a program that plots the function y = x2.

# Author: Eva Cz-P.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints  # multiply each entry by itself, or could use xpoints ** 2

plt.plot(xpoints, ypoints)
plt.show()


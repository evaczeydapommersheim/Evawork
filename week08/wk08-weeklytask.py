# This program is to experiemnt with matplotlib and try different solutions for the week08 weekly task 
#Author: Eva Cz-P.

import matplotlib
print(matplotlib.__version__)
import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints, marker = 'h')
plt.show()

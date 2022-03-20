# Write a program that makes a list called ages that has, the same number random
# values as salaries, (range:21 to 65) . Make scatter plot of this data
# Add a line to this plot that shows y= x2 in a different colour

# Author: Eva Cz-P.

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)

minSalary = 20000
maxSalary = 80000
minAge = 21
maxAge = 65
numberOfEntries = 100

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)

plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints ** 2  # multiply each entry by itself, or could use xpoints ** 2

plt.plot(xpoints, ypoints, color = 'r')
plt.show()
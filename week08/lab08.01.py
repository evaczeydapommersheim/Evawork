# This program is creating s a list, called salaries,
#  that has (say 10) random numbers (20000 – 80000).

# Author: Eva Cz-P.

import numpy as np # use numpy to create this list of randon numbers.
# setting the values available for the variables in advance is beneficial
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

print(salaries)
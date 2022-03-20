# This program is creating s a list, called salaries,
#  that has (say 10) random numbers (20000 – 80000).

import numpy as np # use numpy to create this list of randon numbers.
# setting the values available for the variables in advance is beneficial

# Author: Eva Cz-P.


minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)       # this is so that the "random" numbers are the same each time to make it easier to debug.

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)  

print(salaries)
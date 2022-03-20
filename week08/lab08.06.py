# Write a program that plots a histogram of the salaries (from Question 1)
# Author: Eva Cz-P.

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)

plt.hist(salaries, color = 'g')
plt.title('Salaries')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()


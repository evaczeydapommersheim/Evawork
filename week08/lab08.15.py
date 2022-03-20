# . Add a line of normal distribution to the plot in 9 above. (use seaborn)
# Author: Eva Cz-P.


import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
import seaborn as sns

minSalary = 20000
maxSalary = 80000
minAge = 21
maxAge = 65
numberOfEntries = 100

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)

plt.scatter(ages, salaries, label='Salaries')

xpoints = np.array(range(1, 101))
ypoints = xpoints ** 2  # multiply each entry by itself, or could use xpoints ** 2

plt.plot(xpoints, ypoints, color = 'r', label='x squared')
plt.title('Random Plot')
plt.xlabel('Age')
plt.ylabel('Salaries')
plt.legend()


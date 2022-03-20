# Save this to a file called “prettier-plot.py”

# Author: Eva Cz-P.

#add this line to the end and you can comment out the show()
#plt.show() # see how the axis have changed

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

plt.scatter(ages, salaries, label='Salaries')

xpoints = np.array(range(1, 101))
ypoints = xpoints ** 2  # multiply each entry by itself, or could use xpoints ** 2

plt.plot(xpoints, ypoints, color = 'r', label='x squared')
plt.title('Random Plot')
plt.xlabel('Age')
plt.ylabel('Salaries')
plt.legend()

# plt.show()
plt.savefig('Prettier-plot.png')
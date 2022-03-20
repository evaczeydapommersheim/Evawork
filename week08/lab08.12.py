# Write program that has a list of counties, make it a long list (pick from five
# counties). Make some counties appear more than others. Make a pie chart of the
# counties.
# 12. Modify the program to make bar chart of the counties.

#Author: Eva Cz-P.

import numpy as np
import matplotlib.pyplot as plt

# making the array of occurrences

possibleCounties = ['Mayo', 'Galway', 'Roscommon', 'Kerry', 'Cork']

# pick 100 randomly from the possible counties list [] with the frequence set in 'p'
counties = np.random.choice(
    possibleCounties,
    p=[0.1, 0.3, 0.2, 0.12, 0.28], 
    size=(100)
)
# right now we need the number of occurences of each county
# this returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

# we can now put this into a bar chart
plt.bar(unique, counts)

plt.show()
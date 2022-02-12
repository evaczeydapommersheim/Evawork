# generates 10 random numbers (0-100)
# prints them out
# then prints out the top three.

# Author: Eva Czeyda-Pommersheim

import random

randomNumber = []
for i in range(0,10):
    randomNumber.append(random.randint(1,101))

print(randomNumber)

top3 = randomNumber.copy()
top3.sort(reverse = True)
print(top3)
print ("The top 3 are \t {}".format(top3[0:3]))
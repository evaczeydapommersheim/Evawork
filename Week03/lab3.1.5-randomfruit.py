#This program prints out a random fruit
#Author: Eva Czeyda-Pommersheim

import random

fruits = ["apple", "Orange", "Pineapple", "Banana", "Pear", "Mango"]

#lists are indexed starting from 0 until the last item counted. The index needs to be defined to ensure all fruits (listed items) are included in the random selection.
#it is not the fruit as a string that is selected but the index of the fruit within the list, therefore new variable fruit is required.

index = random.randint(0, len(fruits)-1)
fruit = fruits[index] #not quite sure about what the [] means here???
print(("A random fruit is {}".format(fruit)))
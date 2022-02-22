# This program puts 10 random numbers into a queue and outputs as a list
# the program then takes the first number from the queue and lists the remaining numbers in the queue, doing this one at a time
# repeat this loop until the last number is taken from the queue
# Print "The queue is now empty"

# Author: Eva Czeyda-Pommersheim

import random

numbers = random.sample(range(0, 100), 10)  
# sample() method is available in the random module and can generate a list of 10 random numbers within a range (0 and 100) 
# Source used: https://www.tutorialspoint.com/generating-random-number-list-in-python

print("The queue is", numbers) # this will list the 10 random numbers.

while len(numbers) != 0: #while look is used to ensure that this step is repeated until the list is empty, i.e. length is = 0.
    currentNumber = numbers.pop(0)
    print("The current number is",currentNumber, "and the queue is", numbers)

print("The queue is now empty")
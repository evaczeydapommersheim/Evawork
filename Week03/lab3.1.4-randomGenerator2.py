# Allow user to enter the range a random number is to be returned from
# start is the first value of the range
#stop is the last value of the range, this will not be included as a possible value

start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))

import random
number = random.randrange(start,stop)
print("Here is a random number of the given range: {}".format(number))
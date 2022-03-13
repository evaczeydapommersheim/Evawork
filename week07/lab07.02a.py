# this is to create a function that reads in a number from a file that already exists (count.txt)
# Author: Eva Cz-P.

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
# in order to test the function
num = readNumber()
print(num)
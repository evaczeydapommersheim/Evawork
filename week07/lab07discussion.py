# this program will check if the file exists and will 
# also initialize the file by running the writeNumber() function
# by entering 0

#Author: Eva Cz-P.

def writeNumber(number):
    with open("count.txt", "wt") as f:
        f.write(str(number)) 

import os
filename = "count.txt"
if not os.path.isfile(filename):
    print("File does not exist!")
writeNumber(0)

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0
num = readNumber()
print(num)
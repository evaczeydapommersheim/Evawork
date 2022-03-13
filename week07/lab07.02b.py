# this is to create a function that takes in a number 
# and overwrites the file (count.txt) with that number
# Author: Eva Cz-P.

filename = "count.txt"
def writeNumber(number):
    with open("count.txt", "wt") as f:
        f.write(str(number)) 
        #write only takes a string, therefore the integer entered under readNumber needs to be converted to a string
        #in order to text the function
writeNumber(3)
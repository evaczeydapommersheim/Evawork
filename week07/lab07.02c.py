# program uses these two functions, to count how many times
# the program has been run. Test it, check to see that the number goes up
# each time

#Author: Eva Cz-P.

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open("count.txt", "wt") as f:
        f.write(str(number)) 
        #write only takes a string, therefore the integer entered under readNumber
        # needs to be converted to a string

# main program under Q2b. number overwrote number zero in the file. 
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)

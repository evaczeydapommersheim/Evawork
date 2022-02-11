# This program asks the user to enter a number and return the result whether it is even or odd
#it will keep prompting the user to enter a number until -1 is entered, upon which program will quit

# Author: Eva Czeyda-Pommersheim

number = int(input("Enter an integer: (-1 to quit):"))

while number > -1:
    if (number % 2) == 0:
        print("{} is an even number!".format(number))
    else:
        print("{} is an odd number!".format(number))
    number = int(input("(enter -1 to quit): "))
print("End of the program")
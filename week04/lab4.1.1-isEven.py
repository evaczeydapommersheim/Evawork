# This program asks the user to enter a number and return the result whether it is even or odd

# Author: Eva Czeyda-Pommersheim

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print("{} is an even number!".format(number))
else:
    print("{} is an odd number!".format(number))
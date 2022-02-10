# This program divides one number from another, it returns the amount in integer and the remainder separately
# Author:Eva czeyda-Pommersheim

x = int(input("Enter first number "))
y = int(input("Enter the number you want to divide by "))
answer = int(x//y)
remainder = x%y
print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))
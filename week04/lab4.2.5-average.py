#keeps reading numbers until the user enters a 0. (the program should append each of them into a list)
# The program then prints out each of the numbers entered 
# and the average of them.

# Author: Eva Czeyda-Pommersheim

numbers = []

number = int(input("Please enter a number (0 is to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Please enter a number (0 is to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print("The average is", average)
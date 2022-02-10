# This program does the following:
# reads the input string
# strips any leading and trailing spaces from the input string and converts the input string to lower case as an output string
# outputs the length of the input and the output string

# Author: Eva Czeyda-Pommersheim

inputString = input("Please enter a string: ")
outputString = inputString.strip()
normalizedString = outputString.lower()

lengthOfInputString = len(inputString)
lengthNormalizedString = len(outputString)

print("That String normalized is: {}".format(normalizedString))
print("The input string got reduced from {} to {} characters.".format(lengthOfInputString, lengthNormalizedString))
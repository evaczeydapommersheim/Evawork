# This program prompts the user to guess a number, 
# the program keeps prompting the user to guess the number 
# until the user gets the right answer

# Author: eva Czeyda-Pommersheim

numberToGuess = 28 

number = int(input("Guess a number: ")) # assumption is the only integers will be entered as a guess

while number != numberToGuess:
    print ("Wrong!")
    number = int(input("Guess another number: "))

print("Well Done! Yes, the number was {}".format(numberToGuess))

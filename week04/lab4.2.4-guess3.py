# This program prompts the user to guess a number, 
# the program keeps prompting the user to guess the number 
# until the user gets the right answer
# while giving a hint if the number guessed is too low or too high to the number to be guessed

# Author: eva Czeyda-Pommersheim

numberToGuess = 28 

import random #program to generate a random number

number = random.randint(1, 100) # assumption is the only integers will be entered as a guess

while number != numberToGuess:
    if number < numberToGuess:
        print ("{} is Too Low!".format(number))
    else:
        print ("{} is Too high!".format(number))
    number = random.randint(1, 100)

print("Well Done! Yes, the number was {}".format(numberToGuess))

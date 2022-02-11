# This program prompts the user to guess a number, 
# the program keeps prompting the user to guess the number 
# until the user gets the right answer
# while giving a hint if the number guessed is too low or too high to the number to be guessed

# Author: eva Czeyda-Pommersheim

numberToGuess = 28 

number = int(input("Guess a number: ")) # assumption is the only integers will be entered as a guess

while number != numberToGuess:
    if number < numberToGuess:
        print ("Too Low!")
    else:
        print ("Too high!")
    number = int(input("Guess another number: "))

print("Well Done! Yes, the number was {}".format(numberToGuess))

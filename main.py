#import libraries
import random

#variables
realWord = SUPER
guessedWord = ""

#main code

guessedWord = input("Guess the word")
while len(guessedWord) != 5:
    guessedWord = input("Invalid input, try again")

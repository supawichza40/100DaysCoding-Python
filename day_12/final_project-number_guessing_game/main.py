# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

from numpy import number


def printNumberOfAttemp(number_of_guess):
    print(f"You have {number_of_guess} attemps remaining to guess the number.")


def isHigherOrLower(user_input, chosen_number, number_of_guess):
    if(user_input < chosen_number):
        print("Too Low")
        number_of_guess -= 1
        return number_of_guess
    elif(user_input > chosen_number):
        print("Too High")
        number_of_guess -= 1
        return number_of_guess
    else:
        print("This is the correct answer")
        print(f"The chosen number is {chosen_number}")
        number_of_guess = 0
        return number_of_guess


def revealAnswer(chosen_number):
    print(f"The chosen number is {chosen_number}")


number_of_guess = 0
print("Welcome to the Number Guessing Game!")
chosen_number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if(difficulty == "easy"):
    number_of_guess = 10
else:
    number_of_guess = 5

while(number_of_guess > 0):
    printNumberOfAttemp(number_of_guess)
    user_guess = int(input("Make a guess: "))
    number_of_guess = isHigherOrLower(
        user_guess, chosen_number, number_of_guess)

revealAnswer(chosen_number)

#Step 1 
import random as random

from numpy import number
word_list = ["aardvark", "baboon", "camel"]
user_letter = ""
hangman_step = [
    r"""
    
         
          
          
          
          
    
 ____|___
 """,
 r"""
    
 
           
          
           
          
     |
 ____|___
 """,
 r"""

          
     |      
     |      
     |       
     |      
     |
 ____|___
 """,
 r"""
    ____
     |/      
     |      
     |      
     |      
     |      
     |
 ____|___
 """,
 r"""
    _______
     |/      
     |      
     |      
     |       
     |      
     |
 ____|___
 """,
 r"""
    _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
 ____|___
 """,
 r"""
    _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|___
 """,
  r"""
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 ____|___
 """,
 
]
number_of_lives = 0
hangman_logo = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
"""
#Introduction

print(hangman_logo)
print("Welcome to my Supavich Hangman game!")
#End of introduction
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[random.randint(0,len(word_list)-1)]
for _ in chosen_word:
    user_letter+="_"

while("_" in user_letter and number_of_lives<len(hangman_step)-1 ):
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess_letter = input("Guess the letter: ").lower()
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    if(guess_letter in chosen_word):
        #loop through chosen word and compare if the guess letter match any letter
        for index in range(0,len(chosen_word)):
            if(guess_letter==chosen_word[index]):
                #create a new string with chosen character
                user_letter = user_letter[:index] + guess_letter + user_letter[index+1:]
        print(user_letter)
        print(hangman_step[number_of_lives])
        
    else:
        number_of_lives+=1
        print(user_letter)
        print(hangman_step[number_of_lives])
        
if(number_of_lives>=len(hangman_step)-1):
    print("You lose! No more lives")
else:
    print(f"You win! The word is {chosen_word}")

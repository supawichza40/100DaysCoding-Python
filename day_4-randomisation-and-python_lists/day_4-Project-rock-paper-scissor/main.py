rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissor_list = [rock,paper,scissors]
#Write your code below this line 👇
import random as random
#user input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You choose")
print(rock_paper_scissor_list[user_input])
#end of user input
print("VS")
#generate random computer input 
computer_generate_number = random.randint(0,2)
print("Computer Choose")
print(rock_paper_scissor_list[computer_generate_number])
#end of computer input
#Logic to find out who is the win, lose or draw.
if(user_input==computer_generate_number):
    print("This is a draw")
elif((user_input==0 and computer_generate_number==2) or (user_input==2 and computer_generate_number==0)):
    if(user_input==0):
        print("You win!")
        print("Computer Lose!")
    else:
        print("Computer win!")
        print("You lose!")
else:
    if(user_input>computer_generate_number):
        print("You win!")
        print("Computer Lose!")
    else:
        print("Computer win!")
        print("You lose!")
#end of logic
        
    
        
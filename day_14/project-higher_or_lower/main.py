import os 
import game_data
import art
import random
def clear():
    os.system("cls")
   
    
def isCorrectAnswer(a,b,user_answer):
    if(user_answer=='a' and a["follower_count"]>b["follower_count"]):
        return True
    elif(user_answer == "b" and a["follower_count"]<=b["follower_count"]):
        return True
    else:
        return False
    
    
player_score = 0

right_answer =True
while(right_answer):
    print(art.logo) 
    if(player_score>0):
        print(f"You're right! Current Score:{player_score}")
    compare_a = random.choice(game_data.data)
    compare_b = random.choice(game_data.data)
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(f"\n{art.vs}")
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    right_answer = isCorrectAnswer(compare_a,compare_b,user_answer)
    if(right_answer):
        player_score+=1
    clear()
    
print(f"Sorry, that's wrong. Final Score: {player_score}")
        

    

import os

from numpy import where
import art as logo
def clear():
    os.system("cls")

print(logo.logo)

list_of_player = []
more_player = True

while(more_player==True):
    user_name = input("What is your name?")
    bid_price = int(input("What is the bid price?"))
    list_of_player.append({"name":user_name,"bid":bid_price})
    more_player = bool(int(input("would you like to add more player?'yes=1'/'no=0'")))
    clear()
    
list_of_player.sort(key= lambda player:player["bid"],reverse=True)
print("The winner of this bid is.......")
print(f"{list_of_player[0]['name']} with a bid of ${list_of_player[0]['bid']}")




from audioop import getsample
import art 
import random
print(art.logo)

card_dict = {
    "card":{"1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "J":10,
            "Q":10,
            "K":10}
}
yes_or_no = {
    "y":1,
    "n":0
}
card_list = list(card_dict["card"].keys())
user_card = []
computer_card = []
#assign card_dict to user_card
for _ in range(0,2):
    user_card.append(random.choice(card_list))
    computer_card.append(random.choice(card_list))


def show_card():
    print("Your card")
    print(user_card)
    print("Computer card")
    print(f"['{computer_card[0]}', '*']")
    
def deal_card():
    user_card.append(random.choice(card_list))
    if(getCardSum(user_card)>21):
        findingWinner()
        return
    if(getCardSum(computer_card)<18):
        computer_card.append(random.choice(card_list))
        
    
def getCardSum(player_or_computer):
    sum = 0
    for card in player_or_computer:
        sum +=card_dict["card"][card]
    return sum
#Logic for comparing card and find winner
def findingWinner():
    if(getCardSum(user_card)==getCardSum(computer_card)):
        print("This is a draw")
    elif(getCardSum(user_card)>getCardSum(computer_card) and getCardSum(user_card)<=21):
        print("You are a winner!")
        show_card()
        print(f"You {getCardSum(user_card)} VS Computer {getCardSum(computer_card)}")
    else:
        print("Computer is a winner!")
        show_card()
        print(f"You {getCardSum(user_card)} VS Computer {getCardSum(computer_card)}")
    


show_card()
another_card = bool(int(yes_or_no[input("Type 'y' to get another card, type 'n' to pass: ")]))
if(another_card):
    while(getCardSum(user_card) and another_card):
        deal_card()
        if(getCardSum(user_card)>21):
            break
        show_card()
        another_card = bool(int(yes_or_no[input("Type 'y' to get another card, type 'n' to pass: ")]))
        
findingWinner()
        

    

        
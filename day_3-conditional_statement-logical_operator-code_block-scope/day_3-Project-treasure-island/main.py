treasure_art = r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/\####/       /
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

'''
print(treasure_art)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
option1 = input("You coming up on the cross road, Do you want to go left or right?left or right: ")
if(option1=="left"):
    option2 = input("You reach the end of the land.You have option to wait until the sun is down or swim?wait or swim: ")
    if(option2=="wait"):
        print("After you wait till sun down, there was a light emit from the sea.")
        option3 = input("There is 3 doors appear in front of you. Which door would you choose?red,yellow,blue door: ")
        if(option3=="red"):
            print("You got burned by the fire.")
        elif(option3=="blue"):
            print("You got eaten by a beasts\nGame Over!")
        elif(option3 == "yellow"):
            print("You found the hidden treasure behind the yellow door.")
            print("and live a life of luxery");
        else:
            print("Game Over.")
    else:
        print("You got attacked by trout. and eaten you alive!\nGame Over!.")
else:
    print("Fall into a hole\nGame Over.")


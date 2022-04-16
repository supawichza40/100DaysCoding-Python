#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as name:
    with open("./Input/Letters/starting_letter.txt") as letter:

        name = name.readline()
        while(name!=""):
            letter_content = letter.read()
            letter_content.replace(__old= "name" ,__new=name)
            with open(f"letter_to_{name}.txt","w") as letter_save:
                letter_save.write(letter_content)



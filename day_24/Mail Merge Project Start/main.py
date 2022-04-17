#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as name:
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        name_content = name.readline()

        while(name_content!=""):
            
            name_removed_n = name_content.strip("\n")
            with open(f"./Output/ReadyToSend/{name_removed_n}.txt","w") as new_letter:
                new_content = letter_content.replace("[name]",name_removed_n)
                new_letter.write(new_content)
                name_content = name.readline()





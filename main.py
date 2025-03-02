#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    user_name = names

    for user in user_name:
        new_user = user.strip()
        with open("./Input/Letters/starting_letter.txt") as letter:
            for i in letter:
                new_letter = i.replace("[name]", new_user)
                with open(f"./Output/ReadyToSend/{new_user}.txt", mode="a") as invites:
                    invites.write(new_letter)





#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PERSONALIZED_NAME = "[name]"

with open("Input/Letters/starting_letter.txt") as data:
    letter = data.read()

with open("Input/Names/invited_names.txt") as name:
    names = name.readlines()

for inv in names:
    stripped_name = inv.strip()
    personalized_letter = letter.replace(PERSONALIZED_NAME, stripped_name)
    with open(f"Output/ReadyToSend/{stripped_name}.txt", mode="w") as invite:
        invite.write(personalized_letter)
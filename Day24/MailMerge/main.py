#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# open invite list
with open("./Input/Names/invited_names.txt") as names:
    invitelist = names.readlines()

# open letter template
with open("./Input/Letters/starting_letter.txt") as letter:
    message = letter.read()

# for each of the invites on invite list
# replace [name] in letter template with invite person
# write the letter to a file for that person
for invite in invitelist:
    person = invite.strip("\n")
    merge_mgs = message.replace(PLACEHOLDER, person)
    # print(merge_mgs)
    filename = f"./Output/ReadyToSend/letter_for_{person}.txt"
    with open(filename, mode="w") as invitation:
        invitation.write(merge_mgs)

# Just print that we are done
print ("Finished!")



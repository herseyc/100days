# Number Guessing Game Objectives:
import random

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print("Welcome to the number game!")

def number_game(difficulty):
    #Computer picks a random number between 1 and 100
    computer_num = random.randint(1, 100)

    #Set difficulty
    if difficulty == "easy":
        turns = 10
    else:
        turns = 5

    #Use this to debug
    #print(f"The computer picked: {computer_num}")
    # Track the number of turns left
    turns_left = turns

    #Loop until player guesses the number or runs out of turns
    while turns_left:
        for turn in range(turns):
            player_guess = int(input("Make a guess: "))
            # Decrease turns left
            turns_left -= 1
            # Check player's guess against computer number
            if player_guess == computer_num:
                print("Player Wins!")
                return

            elif player_guess < computer_num:
                print("Too low.")

            elif player_guess > computer_num:
                print("Too high")

            # If there are turns left print attempts left
            if turns_left > 0:
                print(f"You have {turns_left} attempts remaining to guess the number")
            else:
                print("You've run out of guesses. You lose!")
                return


#Keep the game going
quit_game = False

while not quit_game:
    print("I am thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' or 'quit': ")
    if difficulty == "quit":
        quit_game = True
        print("Bye Bye!")
    else:
        number_game(difficulty)
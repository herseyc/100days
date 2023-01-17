import random

# Set Constants for HARD and EASY Difficulty
HARD_DIFFICULTY = 5
EASY_DIFFICULTY = 10

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#Computer picks a number
answer = random.randint(1, 100)

def set_difficulty():
    #Set game difficulty
    level = input("Chose Difficulty, enter 'easy' or 'hard': ")
    if level == "easy":
        return EASY_DIFFICULTY
    else:
        #If player enters anything other than easy, set difficulty to HARD
        return HARD_DIFFICULTY

def check_answer(guess, answer, turns):
    """Takes guess, answer, turns and returns turns - 1"""
    #Check answer and take off turns
    #Testing
    #print(guess, answer, turns)

    if guess < answer:
        print("Too Low!")
        return turns - 1
    elif guess > answer:
        print("Too High!")
        return turns - 1
    else:
        print(f"You got it! The number I was thinking of was {answer}")

def game():
    turns = set_difficulty()

    guess = 0
    # If the guess does not equal the answer keep asking until you run out of turns.
    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Your Guess: "))
        turns = check_answer(guess, answer, turns)

        # Are there turns left?
        if turns == 0:
            print(f"You have run out of turns. The number I was thinking of was {answer}. You lose!")
            return
        elif guess != answer:
            print("Guess again.")

# Run the game
game()
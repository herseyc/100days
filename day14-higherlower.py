import random
from day14gamedata import data


def account(compare, pick):
    """Takes string compare (A or B) and pick to print name, description and country"""
    print(f"Compare {compare}: {data[pick]['name']}, a {data[pick]['description']}, from {data[pick]['country']}")


# pick higher or lower
def check_guess(high, low):
    """Takes guessed high (high) and the low pick.  Compares them, returns the high pick if correct, or False if not."""
    if data[high]["follower_count"] > data[low]["follower_count"]:
        return high
    # Return False - you lose.
    return False

def chose_rand():
    picked = random.randint(0, len(data) - 1)
    return picked

pick_A = chose_rand()

# set ingame to True, ingame False will break the while loop
ingame = True
# set score count to 0
count = 0

while ingame:

    account("A", pick_A)
    # DEBUG
    # print(f"Followers {data[pick_A]['follower_count']}")

    print("\nvs\n")

    pick_B = chose_rand()

    #just in case pick_B and pick_A are equal
    while pick_B == pick_A:
        pick_B = chose_rand()

    account("B", pick_B)
    # DEBUG
    # print(f"Followers {data[pick_B]['follower_count']}")

    guess = input("\nWho has the higher follower count 'A' or 'B': ")

    if guess == "A" or guess == "a":
        # Is pick_A higher than pick_B
        check = check_guess(pick_A, pick_B)
    else:
        # Is pick_B higher than pick_A
        check = check_guess(pick_B, pick_A)

    if check:
        # Set pick_A to check
        pick_A = check
        # Add one to score count
        count += 1
        # Print the current score
        print(f"Correct! Your current score is: {count}")
    else:
        # You got it wrong, end the loop
        ingame = False

# Show the final score
print(f"\nWrong! Your final score was: {count}")
print("Bye!")

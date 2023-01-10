import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

player_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

if player_hand >= 3 or player_hand < 0:
    print("Invalid Input! You Lose!")
else:
    print(hands[player_hand])

    # Computer choice
    computer_hand = random.randint(0, 2)
    print("Computer chose:")
    print(hands[computer_hand])

    # Check who wins
    # player == computer draw
    # rock [0] beats scissors [2]
    # scissors [2] beats paper [1]
    # paper [1] beats rock [0]

    if player_hand == computer_hand:
        print("It's a draw.")
    elif player_hand == 0 and computer_hand == 2:
        print("Player Wins!")
    elif player_hand == 2 and computer_hand == 1:
        print("Player Wins!")
    elif player_hand == 1 and computer_hand == 0:
        print("Player Wins!")
    else:
        print("Computer Wins! You Lose!")
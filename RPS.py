import random

print("rock, paper, scissors game")

player = input("player 1, please choose 'rock', 'paper' or 'scissors': >>> ").lower()

random_number = random.randint(0, 2)


if random_number == 0:
    computer = "rock"
elif random_number == 1:
    computer = 'paper'
else:
    computer = "scissors"
    print(f"computer plays {computer}")
if player == computer:
    print("draw")
elif player == 'rock' and computer == 'scissors':

    print('player one wins')
elif player == 'paper' and computer == 'rock':

    print('player one wins')
elif player == 'scissors' and computer == 'paper':

    print('player one wins')
else:

    print('computer wins')


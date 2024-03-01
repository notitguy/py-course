import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    playerChoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper or \n3 for Scisoors:\n\n")

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computerChoice = random.choice("123")

    computer = int(computerChoice)

    print('\nYou chose ' + str(RPS(player).name) + '.')
    print('Python chose ' + str(RPS(computer).name) + '.\n')

    if player == 1 and computer == 3:
        print('🎉 You win!')
    elif player == 2 and computer == 1:
        print('🎉 You win!')
    elif player == 3 and computer == 2:
        print('🎉 You win!')
    elif player == computer:
        print("🤷‍♂️ Tie game")
    else:
        print('🐍 Python wins!')
    playagain = input("\nPlay again? \nY or \nN \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉 🎉 🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 😏")

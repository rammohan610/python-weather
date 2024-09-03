import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    print("")
    playerchoice = input(
        "Enter...\n1 for Rock\n2 for Paper\n3 for Scissors\n"
    )

    player = int(playerchoice)

    if player not in (1,2,3):
        sys.exit("You Must enter 1, 2 or 3")
    
    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print(str(RPS(player)).replace("RPS.","").title())

    if playerchoice == "1":
        playerchoiceword = "ROCK"
    elif playerchoice == "2":
        playerchoiceword = "PAPER"
    else:
        playerchoiceword = "SCISSORS"
    
    if computerchoice == "1":
        computerchoiceword = "ROCK"
    elif computerchoice == "2":
        computerchoiceword = "PAPER"
    else:
        computerchoiceword = "SCISSORS"

    print("")
    print("You chose " + playerchoiceword + ".")
    print("Python chose " + computerchoiceword + ".")
    print("")

    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie Game!")
    else:
        print("Python wins!")

    playagain = input("\nPlay Again? (Y/N) \n\n")

    if playagain.lower() == 'y':
        continue
    else:
        print("Thank You for Playing!")
        playagain = False
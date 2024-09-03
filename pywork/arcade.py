import sys
import random
from enum import Enum
from rps import rps
from guess_number import guess_number as gmn

def arcade(name = "PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back:
            print(f"{name}, Welcome back to the Arcade Menu.")
            
        playerchoice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nor press 'x' to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x", "X"]:
            print(f"{name}, please you must enter 1 or 2")
            return arcade(name)
        
        welcome_back = True

        if playerchoice == "1":
            game1 = rps(name)
            game1()
        elif playerchoice == "2":
            game2 = gmn(name)
            game2()
        else:
            print("Thank You for Playing!")
            sys.exit(f"Bye {name}! 👋")

    
if (__name__) == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()
    
    arcade(args.name)
    
import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            "Enter...\n1 for Rock\n2 for Paper\n3 for Scissors\n"
        )

        if playerchoice not in ["1", "2","3"]:
            print("You must enter 1, 2 or 3")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        
        print(f"\nYou chose {str(RPS(player)).replace("RPS.","").title()}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.","").title()}.\n")

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "🎉 You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "🎉 You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "🎉 You win!"
            elif player == computer:
                return "👉🏽👈🏽 Tie Game!"
            else:
                python_wins += 1
                return "🐍 Python wins!"
        
        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer Wins: {str(player_wins)}")
        print(f"\nPython Wins: {str(python_wins)}")

        playagain = input("\nPlay Again? (Y/N) \n\n")

        if playagain.lower() == 'y':
            return play_rps()
        else:
            print("Thank You for Playing!")

    return play_rps

      
play = rps()

play()
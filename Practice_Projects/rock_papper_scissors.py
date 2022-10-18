import random

def game():

    while True:

        player_move = input("Rock (R), Paper (P) or Scissers (C)? ")
        cpu_move = random.choice(["r", "p", "c"])
        
        if player_move == cpu_move:
            print("Draw!")
        
        elif player_move == "r" and cpu_move == "p":
            print("Player lost! Rock loses to Paper!")

        elif player_move == "r" and cpu_move == "c":
            print("Player won! Rock beats Scissers!")
        
        elif player_move == "p" and cpu_move == "r":
            print("Player won! Paper beats Rock!")
        
        elif player_move == "p" and cpu_move == "c":
            print("Player lost! Paper loses to Scissers!")

        elif player_move == "c" and cpu_move == "r":
            print("Player Lost! Scissors loses to Rock!")
        
        elif player_move == "c" and cpu_move == "p":
            print("Player won! Scissors beats Paper!")
        else:
            print("Need a valid move.")

game()
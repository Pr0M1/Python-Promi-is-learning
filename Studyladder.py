import random

def username(): # Username checker
    while True:
        print("Welcome, what is your name?")
        userr = input()
        if userr == "d":
            print("Welcome " + userr + ".")
            break
        elif userr != "d":
            print("Access denied, wrong user name!")
            print("Try again.")

def password(): # Password checker
    while True:
        print("Please, type in your password.")
        password = input()
        if password == "d":
            print("Access granted!")
            break
        elif password != "d":
            print("Access Denied")
            print("Try again.")

def rollGame(): # Games mini-program
    print("Roll the dice!")
    print("To roll, type: 'roll'.")
    print("If you wish to quit, please type: 'quit'")

    wins = 0
    losses = 0
    ties = 0

    while True: # Main Game loop
        print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties,))
        while True: # Player input loop
            playerInput = input()
            if playerInput == "roll":
                break
            elif playerInput == "quit":
                return # Goes back to the "terminal".
            elif playerInput != "roll" or playerInput != "quit":
                print("Please type in a valid command.")
        
        # Players random roll
        if playerInput == "roll":
            playerRoll = random.randint(1,6) 
            if playerRoll == 1:
                print("Player: One")
            elif playerRoll == 2:
                print("Player: Two")
            elif playerRoll == 3:
                print("Player: Three")
            elif playerRoll == 4:
                print("Player: Four")
            elif playerRoll == 5:
                print("Player: Five")
            elif playerRoll == 6:
                print("Player: Six")

        #Computers random roll
        compRoll = random.randint(1, 6)
        if compRoll == 1:
            print("Opponent: One")
        elif compRoll == 2:
            print("Opponent: Two")
        elif compRoll == 3:
            print("Opponent: Three")
        elif compRoll == 4:
            print("Opponent: Four")
        elif compRoll == 5:
            print("Opponent: Five")
        elif compRoll == 6:
            print("Opponent: Six")

        # Display and record the win/loss/tie ration
        if compRoll == playerRoll:
            print("It is a tie!")
            ties = ties + 1
        elif playerRoll > compRoll:
            print("You win!")
            wins = wins + 1
        elif playerRoll < compRoll:
            print("You lose!")
            losses = losses + 1

print("Accessing terminal.")
username()
password()
while True:
    print("Hello")
    print("Entering mainframe.")
    print("To exit type: 'goodbye'")
    print("If you wish to play a game type: 'rollgame'")
    pickCommand = input()
    if pickCommand == "goodbye":
        print("Exiting system. Have a nice day.")
        break
    elif pickCommand == "rollgame":
        rollGame()

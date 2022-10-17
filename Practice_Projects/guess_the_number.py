import random

def guess_the_number(x):

    comp_number = random.randint(1, x)

    guess = 0

    while guess != comp_number:

        guess = int(input(f"Give me a number between 1 and {x}: "))

        if guess < comp_number:
            print("Guess again. Too low.")
        elif guess > comp_number:
            print("Guess again. Too High.")
    
    print(f"Grat, you guessed {comp_number}")

def comp_guesses(x):

    low = 1
    high = x
    feedback = ""

    while feedback != "c":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 

        feedback = input(f"Is {guess} to high (H), low (L) or or correct (C)?: ")

        if feedback == "h":
            high = guess -1

        elif feedback == "l":
            low = guess + 1
    
    print(f"Yay! Computer guessed your number, {guess}, correctly")


comp_guesses(20)

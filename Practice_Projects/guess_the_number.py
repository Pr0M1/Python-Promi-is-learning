import random

comp_number = random.randint(1, 2)

while True:

    my_guess = input("Give me a number: ")

    if my_guess == comp_number:
        print("You guessed my number!")
    elif my_guess != comp_number:
        print("Wrong number, try again.")
    else:
        print("Give me a number.")
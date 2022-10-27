import random
from unittest import skip
from words import word
import string

def valid_word(words):

    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangedman(words):

    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print("You have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used that character. Please try again. ")
        
        else:
            print("Invalid character. Please try again. ")


#hangedman(word)


opt_numbers = [1, 2, 3]
tries = int()

while True:

    reaction = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }

    guess = int(input("Guess a number: "))

    if tries in reaction:
        if reaction == 5:
            print(reaction[tries])
            break
        print(reaction[tries])
        continue

    elif guess in opt_numbers:
        print("You guessed it.")
        break
    elif guess not in opt_numbers:
        print("Wrong guess.")
        tries = tries + 1
    
    
import random
from unittest import skip
from words import word
import string

def valid_word(words):

    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman(words):

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
reaction = {
    0: "You have 5 more chances to guess it right.",
    1: "Frist guess.",
    2: "Second guess",
    3: "Third guess.",
    4: "Fourth guess",
    5: "This was the last guess."
}
while True:

    guess = int(input("Guess a number: "))

    if tries in reaction:

        if tries == 5:
            print(reaction[tries])
            print("You guessed to meny times. Game over.")
            break

        elif guess in opt_numbers:
            print("You guessed it.")
            break

        elif guess not in opt_numbers:
            print("Wrong guess.")
            print(reaction[tries])
            tries = tries + 1
            
    
    
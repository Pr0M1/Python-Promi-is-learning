import random
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
    tries = int() 

    reaction = {
    0: "You have 5 more chances to guess it right.",
    1: "Frist guess.",
    2: "Second guess",
    3: "Third guess.",
    4: "Fourth guess",
    5: "This is the last guess.",
    6: "None"
}

    # getting user input
    while len(word_letters) > 0:
        # letters used
        print("You have used these letters: ", " ".join(used_letters))

        if tries == 6:
            print("You guessed to meny times. Game over.")
            break

        else:    
            word_list = [letter if letter in used_letters else "-" for letter in word]
            print("Current word: ", " ".join(word_list))

            print(reaction[tries])
            user_letter = input("Guess a letter: ").upper()
            tries = tries + 1

            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
            elif user_letter in word_letters:
                word_letters.remove(user_letter)
                tries = tries - 1
            
            elif user_letter in used_letters:
                print("You have already used that character. Please try again. ")
                tries = tries - 1
            
            else:
                print("Invalid character. Please try again. ")

hangman(word)

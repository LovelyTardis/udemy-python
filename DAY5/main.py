'''
    In this day's project I will code a Hangman Game, using more than one function.
    The program will choose a random word from a previously done pull.
    The user will write letters and, if they are in the chosen word, they will appear. If not, the user will lose a live.
'''

import random
import time

# Constant variables
WORDS_POOL = ["sea", "hurt", "world", "night", "imagine", "python", "cyberpunk", "language", "train"]
MYSTERY_WORD = random.choice(WORDS_POOL)
LIVES = 6
CUSTOM_PRINTS = {
    "first_print": "Welcome to Hangman Game! Here is the word you have to find...",
    "word": "{arg}",
    "input_not_letter": "The input MUST be a single character!",
    "letter_in_word": "The letter '{arg}' is in the word. Nice!",
    "letter_not_in_word": "The letter '{arg}' is not in the word...",
    "word_found": "\nCongratulations!\nYou've found the word '{arg}'!",
    "word_not_found": "\nSorry, the word was '{arg}' and you didn't find it...",
    "end_game": "\nThank you for playing this game!\nThe console will close automatically in 60 seconds..."
}


def hangman_game():
    user_word = list(len(MYSTERY_WORD) * "_")
    word_found = False
    used_lives = 0
    str_user_word = get_user_word(user_word)

    print(CUSTOM_PRINTS["first_print"].format(arg=str_user_word))
    while used_lives < LIVES:
        print(CUSTOM_PRINTS["word"].format(arg=str_user_word))
        letter = get_user_input(used_lives)
        try:
            check_user_input(letter)
        except:
            continue
        letter_indexes = letter_indexes_in_word(letter)
        if len(letter_indexes) > 0:
            print(CUSTOM_PRINTS["letter_in_word"].format(arg=letter))
            for index, word in enumerate(user_word):
                for i in letter_indexes:
                    if i == index:
                        swap_letter(user_word, index, letter)
                        str_user_word = get_user_word(user_word)
        else:
            print(CUSTOM_PRINTS["letter_not_in_word"].format(arg=letter))
            used_lives += 1
        if is_win(str_user_word):
            word_found = True
            break
    if word_found:
        print(CUSTOM_PRINTS["word_found"].format(arg=MYSTERY_WORD))
    else:
        print(CUSTOM_PRINTS["word_not_found"].format(arg=MYSTERY_WORD))
    print(CUSTOM_PRINTS["end_game"])
    time.sleep(60)


def get_user_input(used_lives):
    return input(f"\nLives: {LIVES - used_lives}\nType a letter: ")


def get_user_word(user_word):
    return "".join(user_word)


def check_user_input(user_input):
    if user_input.isdigit() or len(user_input) != 1:
        print(CUSTOM_PRINTS["input_not_letter"])
        raise Exception()


def letter_indexes_in_word(input_letter):
    found_indexes = list()
    for index, letter in enumerate(MYSTERY_WORD):
        if letter == input_letter:
            found_indexes.append(index)
    return found_indexes


def swap_letter(user_word, index, letter):
    user_word.pop(index)
    user_word.insert(index, letter)


def is_win(user_word):
    if user_word == MYSTERY_WORD:
        return True
    else:
        return False


hangman_game()

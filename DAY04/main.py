'''
    This day's project will be a simple game that asks the user to input his/her name.
    Then, the program will say that it thought about a number between 1 and 100, and the user
    have eight attempts to guess the correct number. There are four types of answers:
    1. If the input number is not between 1 and 100, the program will redo the question (not losing the try)
    2. If the input number is below the correct one, the user will be warned about that.
    3. If the input number is above the correct one, as before, the user will be warned as well.
    4. If the user guessed the number, win and total attempts message appears.
'''
import random
import time

if __name__ == '__main__':
    # Constant variables
    TOTAL_ATTEMPTS = 8
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    CORRECT_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)

    # Primary input and variables
    user_name = input("What's your name? (default: User)\n") or "User"
    user_number = 0
    counter = 0
    guessed = False
    print(f"\nOkay {user_name}!\nI thought a number between {MIN_NUMBER} and {MAX_NUMBER} (both inclusive).\nCan you guess it?")

    while counter < TOTAL_ATTEMPTS:
        if counter != TOTAL_ATTEMPTS - 1:
            print(f"\nRemaining attempts: {TOTAL_ATTEMPTS - counter}")
        else:
            print(f"\nThis is your last attempt! Think wisely...")
        try:
            selected_number = int(input("Number: "))
        except:
            print("\nPlease, type an integer number.")
            continue
        if selected_number < MIN_NUMBER or selected_number > MAX_NUMBER:
            print(f"\nYou entered an invalid number (This is not counting on you attempts).\nRemember that it has to be between {MIN_NUMBER} and {MAX_NUMBER}")
            continue
        elif selected_number == CORRECT_NUMBER:
            guessed = True
            break
        elif selected_number < CORRECT_NUMBER:
            print(f"The correct number is above {selected_number}")
        elif selected_number > CORRECT_NUMBER:
            print(f"The correct number is below {selected_number}")
        counter += 1
    # End of while clause
    if guessed:
        print(f"\nWOW {user_name}, you did it!\nThe number was {CORRECT_NUMBER} and you guessed it in {counter + 1} attempts!")
    else:
        print(f"\nSorry {user_name}, the correct number was {CORRECT_NUMBER} and you didn't guess it...")
    print("\nThis console will close automatically in 60 seconds. You can close it by yourself too.\nThanks for trying my game!")
    time.sleep(60)

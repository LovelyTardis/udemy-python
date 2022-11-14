'''
    This project is about a program that will ask the user to input a text. Then input 3 letters.
    With all of this, It will do five analysis:
    1. How much times the letters appear in the whole text?
    2. How many words are in the text?
    3. Which are the first and the last words in the text?
    4. Show the text but with all words are inverted.
    5. Is the word 'Python' in the text?
'''

# Inputs and declarations
text = input("Please, write here a text (no limit words)\n")
text_lowered = text.lower()
split_text = text.split(" ")
res_1_count_letters = ""
res_2_total_words = "There are {total_words} words in the text."

for i in range(1, 4):
    selected_letter = input(f"Write your {i} letter: ").lower()
    res_1_count_letters += f"'{selected_letter}' is {text_lowered.count(selected_letter)} time/s in the text.\n"

# 1. How much times the letters appear in the whole text?
print("\n1. How much times the letters appear in the whole text?")
print(res_1_count_letters)

# 2. How many words are in the text?
print("2. How many words are in the text?")
print(res_2_total_words.format(total_words=len(split_text)), "\n")

# 3. Which are the first and the last words in the text?
print("3. Which are the first and the last words in the text?")
print(f"The first letter is '{text[0]}' and the last is '{text[-1]}'.\n")

# 4. Show the text but with all words are inverted.
print("4. Show the text but with all words are inverted.")
split_text.reverse()
joined_split_text = " ".join(split_text)
print(joined_split_text, "\n")

# 5. Is the word 'Python' in the text?
print("5. Is the word 'Python' in the text?")
possible_answers = {True: "Yes", False: "No"}
print(f"{possible_answers['python' in text_lowered]}")

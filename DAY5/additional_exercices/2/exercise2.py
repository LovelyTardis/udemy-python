'''
    This exercise is about a function that receives a word as parameter.
    It returns a list of all letters without repeating any word and all sorted alphabetically.
    Example:
        unique_words_list("integer") -> ["i", "n", "t", "e", "g", "e", "r"] ->
                                     -> ["e", "g", "i", "n", "r", "t"]
'''


def unique_words_list(word=""):
    word_list = list(word)
    result = list(set(word_list))
    result.sort()
    return result


print(unique_words_list("integer"))
print(unique_words_list("entertainment"))

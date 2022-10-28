'''
    The third exercise is about a function that requires an undefined quantity of integer parameters.
    Returns True if in the parameters are two consecutive zeros, else return False.
    Example:
        two_consecutive_zeros(1, 2, 5, 9, 0, 0, 5, 10) -> True
'''

NUMBER_TO_REPEAT = 0


def two_consecutive_zeros(*numbers):
    last_number = NUMBER_TO_REPEAT - 1
    for number in numbers:
        if last_number != NUMBER_TO_REPEAT or last_number != number:
            last_number = number
            continue
        return True
    return False


print(two_consecutive_zeros(1, 2, 5, 9, 0, 0, 5, 10))
print(two_consecutive_zeros(1, 2, 5, 0, 1, 0, 1, 5, 0, 1))

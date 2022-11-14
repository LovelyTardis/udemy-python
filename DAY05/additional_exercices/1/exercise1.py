'''
    This additional exercise is a function that receives three integers as parameters.
    If the sum of all three integers:
        - is above 15, return the highest number it received;
        - is under 10, return the lowest number;
        - is between 10 and 15, return the middle number.
    Example:
        return_distinct(5, 1, 3) -> sum = 9 -> returns 1
'''


def return_distinct(num1, num2, num3):
    total_sum = num1 + num2 + num3
    ordered_numbers = [num1, num2, num3]
    ordered_numbers.sort()
    if total_sum < 10:
        return ordered_numbers[0]
    elif total_sum > 15:
        return ordered_numbers[2]
    else:
        return ordered_numbers[1]


print(return_distinct(5, 1, 3))
print(return_distinct(4, 2, 6))
print(return_distinct(10, 8, 35))

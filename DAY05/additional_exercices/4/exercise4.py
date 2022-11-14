'''
    This additional exercise requests a number as a parameter.
    Returns a list of prime numbers between 2 and the given number (inclusive) and the total quantity of them.
    0 and 1 will not be considered prime numbers.
    Example:
        count_prime_numbers(15) -> return [2, 3, 5, 7, 11, 13], found 6 prime numbers
'''


def count_prime_numbers(number):
    prime_numbers = [2]
    iteration = 3
    step = 2
    while iteration <= number:
        for i in range(3, iteration, step):
            if iteration % i == 0:
                iteration += step
                break
        else:
            prime_numbers.append(iteration)
            iteration += step
    return f"{prime_numbers}, found {len(prime_numbers)} prime numbers"

print(count_prime_numbers(15))
print(count_prime_numbers(100))


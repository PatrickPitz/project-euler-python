"""
The prime factors of 13195 are 5, 7,13 and 29.
What is the largest prime factor of the number 600851475143?
"""


def solution():
    # Only works vor odd numbers
    given_number = 600_851_475_143
    largest_prime_factor = 0
    factor = 3

    while given_number > 1:
        if given_number % factor == 0:
            largest_prime_factor = factor

        while given_number % factor == 0:
            given_number = given_number // factor

        factor += 2
    return largest_prime_factor

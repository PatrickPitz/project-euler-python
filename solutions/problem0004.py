"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solution():
    def is_palindrome(int_to_check):
        int_as_str = str(int_to_check)
        return int_as_str == int_as_str[::-1]

    highest_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            number = i * j
            if is_palindrome(number) and number > highest_palindrome:
                highest_palindrome = number

    return highest_palindrome

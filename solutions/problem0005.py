"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import gcd


def solution():
    num = 1
    for i in range(1, 21):
        num = (num * i) // gcd(num, i)

    return num

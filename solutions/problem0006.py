"""
The sum of the squares of the first ten natural numbers is,
17+2?4...+410? = 385. The square of the sum of the first ten natural numbers is, (1+ 2+...+10)? = 55” = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 — 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def solution():
    n = 100
    sum_of_squares = sum([x * x for x in range(1, n+1)])
    sum_to_n = int((n * n + n) / 2)
    squares_of_sums = sum_to_n * sum_to_n
    return squares_of_sums - sum_of_squares

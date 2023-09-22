"""
The sum of the primes below 10 is 2+ 3+5+ 7=17. Find the sum of all the primes below two million.
"""


def solution():
    sieve = [True for i in range(2_000_000)]
    primes_sum = 0
    for i in range(2, len(sieve)):
        if sieve[i]:
            primes_sum += i
            for j in range(i, len(sieve), i):
                sieve[j] = False
    return primes_sum

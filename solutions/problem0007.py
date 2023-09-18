"""
By listing the first six prime numbers: 2, 3,5, 7,11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


# bruteforce sieve should be much faster
def solution():
    primes = []
    n = 2
    while len(primes) < 10_001:
        is_prime = True
        for i in primes:
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    return primes[-1]

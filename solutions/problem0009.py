"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²,
For example, 3² + 4² = 9+ 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b+ c = 1000. Find the product abc.
"""


def solution():
    def is_triplet(a1, b1, c1):
        return a1 * a1 + b1 * b1 == c1 * c1

    for a in range(1, 1000):
        for b in range(a + 1):
            c = 1000 - a - b
            if c < b:
                break
            if is_triplet(a, b, c) and a + b + c == 1000:
                return a * b * c

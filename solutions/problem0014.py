"""
The following iterative sequence is defined for the set of positive integers:
n —> n/2 (n is even)
n —> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 —> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def solution():
    max_iterations, max_number = 0, 0
    for i in range(1, 1_000_000):
        iterations, tmp_i = 0, i
        while tmp_i > 1:
            iterations += 1
            if tmp_i % 2 == 0:
                tmp_i //= 2
            else:
                tmp_i = 3 * tmp_i + 1
        if iterations > max_iterations:
            max_iterations, max_number = iterations, i

    return max_number


solution()

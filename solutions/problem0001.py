def solution():
    total_sum = 0

    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum
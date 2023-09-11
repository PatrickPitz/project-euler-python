def solution():
    x, y, even_sum = 1, 2, 0

    while x < 4_000_000:
        if x % 2 == 0:
            even_sum += x
        x, y = y, x + y

    return even_sum

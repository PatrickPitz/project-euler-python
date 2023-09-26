"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""


def solution():
    grid_knots = [[1] * 21] * 21
    for row in range(1, 21):
        for column in range(1, 21):
            grid_knots[row][column] = grid_knots[row-1][column] + grid_knots[row][column - 1]
    return grid_knots[20][20]


solution()

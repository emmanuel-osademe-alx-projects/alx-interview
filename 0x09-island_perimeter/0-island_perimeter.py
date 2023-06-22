#!/usr/bin/python3
"""module docs for 0-island_perimeter.py"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with assuming all sides are part of the perimeter
                perimeter += 4
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Deduct 2 for overlapping side
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Deduct 2 for overlapping side
    return perimeter

#!/usr/bin/python3
"""
This module is used to calculate the perimeter
of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid representing the
        map where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
    perimiters = 0
    rows = len(grid)
    cols = len(grid[0])

    for d in range(rows):
        for p in range(cols):
            if grid[d][p] == 1:
                # Check all four possible sides
                if d == 0 or grid[d-1][p] == 0:  # Check up
                    perimiters += 1
                if d == rows - 1 or grid[d+1][p] == 0:  # Check down
                    perimiters += 1
                if p == 0 or grid[d][p-1] == 0:  # Check left
                    perimiters += 1
                if p == cols - 1 or grid[d][p+1] == 0:  # Check right
                    perimiters += 1

    return perimiters
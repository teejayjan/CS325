# Author: Timothy Jan
# Date: 05/18/2021
# Description: Given a 2D grid of 0's (water) and 1's (land), returns how many islands exist in the grid.


def landBF(grid):
    islands = []
    island_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) not in islands and grid[y][x] == "1":
                islands.append((y, x))
                if (y - 1, x) not in islands and (y + 1, x) not in islands and (y, x - 1) not in islands and \
                        (y, x + 1) not in islands:
                    island_count += 1

    return islands, island_count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(landBF(grid))

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(landBF(grid))

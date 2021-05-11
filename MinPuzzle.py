# Author: Timothy Jan
# Date: 05/20/2021
# Description: Given a 3D puzzle, returns, given a minimal effort path from the top left to the bottom right cell,
#              the maximum of the minimal effort path.

import heapq


def minEffort(puzzle, start=(0, 0)):
    """Given a 3D puzzle, returns, given a minimal effort path from the top left to the bottom right cell,the maximum of
     the minimal effort path. Code adapted from my CS 261 Graphs Assignment."""

    visited = {}
    queue = []
    y = 0  # track position in the matrix
    x = 0

    heapq.heappush(queue, ((y, x), 0))  # insert 0,0 with first effort (0)

    while len(queue) > 0:
        cell = heapq.heappop(queue)
        y = cell[0][0]
        x = cell[0][1]
        effort = cell[1]

        if (y, x) not in visited or visited[(y, x)] > effort:
            visited[(y, x)] = effort
            # check up
            if y - 1 > 0:
                effort = abs(puzzle[y - 1][x] - puzzle[y][x])
                heapq.heappush(queue, ((y - 1, x), effort))
            # check down
            if y + 1 < len(puzzle):
                effort = abs(puzzle[y + 1][x] - puzzle[y][x])
                heapq.heappush(queue, ((y + 1, x), effort))
            # check left
            if x - 1 > 0:
                effort = abs(puzzle[y][x - 1] - puzzle[y][x])
                heapq.heappush(queue, ((y, x - 1), effort))
            # check right
            if x + 1 < len(puzzle):
                effort = abs(puzzle[y][x + 1] - puzzle[y][x])
                heapq.heappush(queue, ((y, x + 1), effort))

    return visited


puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))  # 1

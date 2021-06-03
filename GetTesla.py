# Author: Timothy Jan
# Date: 05/31/2021
# Description: Returns the minimum amount of energy needed to take the least-cost path from the upper left to lower
#              right positions in a 2D matrix.


import heapq


def getTesla(M):
    """Given a 2D puzzle with positive and negative numbers, returns the minimum amount of energy needed to take
    the least-cost path from the upper left to the bottom right positions."""

    # populating adjacency matrix code taken from my MinPuzzle.py project
    matrix = {}  # init adjacency matrix

    # populate matrix with all vertices
    for i in range(len(M)):
        for j in range(len(M[0])):
            matrix[(i, j)] = []

    # populate adjacency matrix
    for key in matrix:
        y = key[0]
        x = key[1]
        # up
        if 0 < y < len(M):
            matrix[key].append((y - 1, x))
        # down
        if 0 <= y < len(M) - 1:
            matrix[key].append((y + 1, x))
        # left
        if 0 < x < len(M):
            matrix[key].append((y, x - 1))
        # right
        if 0 <= x < len(M) - 1:
            matrix[key].append((y, x + 1))

    y = 0
    x = 0
    len_y = len(M)
    len_x = len(M[0])
    cost = M[y][x]
    visited = [(y, x)]
    while y != len_y - 1 or x != len_x - 1:
        curr = (y, x)
        curr_neighbors = matrix[curr]
        temp = {}
        for neighbor in curr_neighbors:
            if neighbor not in visited:
                temp[M[neighbor[0]][neighbor[1]]] = neighbor
        next_cost = max(temp)
        cost += next_cost
        next = temp[next_cost]
        visited.append(next)
        y = next[0]
        x = next[1]
    return abs(cost) + 1


# 2
maze = [[-1, -2, 2], [10, -8, 1], [-5, -2, -3]]
print(getTesla(maze))

maze = [[-1, -2, 2], [-5, -8, 1], [10, -2, -3]]
print(getTesla(maze))


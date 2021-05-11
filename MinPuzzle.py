# Author: Timothy Jan
# Date: 05/21/2021
# Description: Given a 3D puzzle, returns, given a minimal effort path from the top left to the bottom right cell,
#              the maximum of the minimal effort path.

import heapq


def minEffort(puzzle):
    """Given a 3D puzzle, returns, given a minimal effort path from the top left to the bottom right cell,the maximum of
     the minimal effort path. Code adapted from my CS 261 Graphs Assignment, CS 325 module,
     and Dijkstra Wikipedia page."""

    matrix = {}  # init adjacency matrix
    prev = {}    # init dictionary to store path taken

    # populate matrix and prev with all vertices
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            matrix[(i, j)] = []
            prev[(i, j)] = None

    # populate adjacency matrix
    for key in matrix:
        y = key[0]
        x = key[1]
        # up
        if 0 < y < len(puzzle):
            matrix[key].append((y - 1, x))
        # down
        if 0 <= y < len(puzzle) - 1:
            matrix[key].append((y + 1, x))
        # left
        if 0 < x < len(puzzle):
            matrix[key].append((y, x - 1))
        # right
        if 0 <= x < len(puzzle) - 1:
            matrix[key].append((y, x + 1))

    # init distances to some large number
    distances = {vertex: float('inf') for vertex in matrix}
    distances[(0, 0)] = 0

    # priority queue
    pq = [(0, (0, 0))]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        # exit if when we've found the path to the bottom right corner
        if current_vertex == (len(puzzle) - 1, len(puzzle) - 1):
            s = []  # array to store shortest path taken
            u = (len(puzzle) - 1, len(puzzle) - 1)  # start at the end
            if prev[u] or u == (0, 0):  # iterate until we're at the beginning
                while u:
                    s.append(u)  # append end point's previous
                    u = prev[u]  # step back to next vertex in the path
            costs = []  # array to store efforts
            for i in range(len(s) - 1):  # iterate through path, storing efforts as we go
                y = s[i][0]
                x = s[i][1]
                y2 = s[i + 1][0]
                x2 = s[i + 1][1]
                costs.append(abs(puzzle[y][x] - puzzle[y2][x2]))
            return max(costs)  # return max of path's efforts

        # from CS 325 module
        for neighbor in matrix[current_vertex]:
            distance = current_distance + puzzle[neighbor[0]][neighbor[1]]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_vertex  # save path taken
                heapq.heappush(pq, (distance, neighbor))


puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))  # 1

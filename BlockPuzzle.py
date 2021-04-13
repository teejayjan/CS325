# Author: Timothy Jan
# Date: 04/12/2021
# CS 325: Analysis of Algorithms
# Description: Finds the number of possible ways one unit and two unit blocks can be arranged to result in a total
#              length N.


def blockpuzzle_dp(N):
    """Determines how many solutions there are to length N made of blocks 1 and 2 units in length."""
    # initialize memo: N = 0 has 0 solutions, N = 1 has 1 solution, N = 2 has 2 solutions
    count_memo = {0: 0, 1: 1, 2: 2}
    for i in range(3, N + 1):
        count_memo[i] = count_memo[i - 1] + count_memo[i - 2]
    return count_memo[N]


def blockpuzzle_bf(N):
    """Brute-force implementation of blockpuzzle."""
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        return blockpuzzle_bf(N - 1) + blockpuzzle_bf(N - 2)


print(blockpuzzle_bf(2))
print(blockpuzzle_bf(3))
print(blockpuzzle_bf(5))
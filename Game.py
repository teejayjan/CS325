# Author: Timothy Jan
# Date: 04/12/2021
# CS 325: Analysis of Algorithms
# Description: Returns True if Player A wins the game. Game starts with player A picking a number i such that
#              0 < i < N and N % i == 0. Player B picks a number j from N-i, such that 0 < j < N - i. This continues
#              until there is no longer a possibility of making a selection (e.g. N = 1).


def game_topdown_helper(N, a_win_conditions):
    """Top-down implementation of the game. Returns True if A wins."""
    # base case: A can't choose an integer 0 < i < 1
    if N == 1:
        return False
    # base case: B can't win when N == 2
    if N == 2:
        return True
    for i in range(1, N):
        if N % i == 0:
            a_win_conditions.append(game_topdown_helper(i, a_win_conditions))
    if True in a_win_conditions:
        return True
    else:
        return False


def game_topdown(N):
    a_win_conditions = []
    return game_topdown_helper(N, a_win_conditions)


for N in range(2, 14):
    print("Top down:", N, game_topdown(N))


def game_bottomup(N):
    """Bottom-up implementation of the game. Returns True if A wins."""
    # Base case where 1 = lose, 2 = win
    memo = {1: False, 2: True}
    for i in range(3, N + 1):
        memo[i] = not memo[i - 1]
    return memo[N]


print()
for N in range(2, 14):
    print("Bottom up:", N, game_bottomup(N))
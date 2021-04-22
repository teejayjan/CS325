# Author: Timothy Jan
# Date: 04/13/2021
# CS 325: Analysis of Algorithms
# Description: Given a set of numbers, returns a subset of non-consecutive numbers that have a maximum sum.


def max_independent_set(nums):
    """Returns a subset of non-consecutive numbers with a maximum sum."""
    length = len(nums)
    sol = [0] * length
    dp = {0: 0}  # store the number choice at each optimal solution
    for i in range(0, length):
        if sol[i - 1] < nums[i] + sol[i - 2]:
            sol[i] = nums[i] + sol[i - 2]
            dp[sol[i]] = nums[i]
        else:
            sol[i] = sol[i - 1]

    # fill solution array
    solution = []
    count = sol[length - 1]  # start at optimal sum
    while count > 0:
        solution.append(dp[count])  # append the number choice at that sum
        count -= dp[count]  # go to the next number choice in that optimal sum
    solution.reverse()
    return solution


arr = [7, 2, 5, 8, 6]
print(max_independent_set(arr))

arr = [1, 100, 6, -8, 7, 9]
print(max_independent_set(arr))

arr = [7, 2, -10, -4, 5, 8, 0, 6, 16, 4]
print(max_independent_set(arr))

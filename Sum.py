# Author: Timothy Jan
# Date: 04/26/2021
# Description: Given two numbers k and n, finds all unique combinations of numbers of length k that add to n.
#              k must be 1 to 9 and numbers in n cannot be repeated. Uses backtracking.

import copy


def combination(sum, length):
    """Given two integers k and n, returns array of all combinations of length k that add to n."""
    result = []
    combination_helper(result, sum, length, [], 1)
    return result


def combination_helper(result, sum, length, combination, start):
    """Helper for combination."""
    # base case
    if sum == 0:
        temp = combination.copy()
        if len(temp) == length:
            result.append(temp)
        return
    elif sum < 0:
        return
    for i in range(start, sum + 1):
        if i not in combination:
            combination.append(i)
        combination_helper(result, sum - i, length, combination, i + 1)
        combination.pop()


# combination(n=sum, k=length)
print(combination(6, 3))
print(combination(9, 3))



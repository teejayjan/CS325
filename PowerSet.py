# Author: Timothy Jan
# Date: 04/14/2021
# CS 325: Analysis of Algorithms
# Description: Given a set of n distinct numbers, returns its power set.


def powerset_helper(pointer, choices_made, input, result):
    if pointer == len(input):
        temp = []
        for num in choices_made:
            temp.append(num)
        result.append(temp)
        return
    choices_made.append(input[pointer])
    powerset_helper(pointer + 1, choices_made, input, result)
    choices_made.pop()
    powerset_helper(pointer + 1, choices_made, input, result)


def powerset(input):
    """Given a set of n distinct numbers, returns its power set."""
    result = []
    powerset_helper(0, [], input, result)
    return result


arr = [1, 2, 3]
print(powerset(arr))
